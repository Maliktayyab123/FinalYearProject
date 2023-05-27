from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from myApp.forms import AdoptChildForm, CommentForm
from myApp.models import AdoptChild, ContactUs, Achievement, Notification, Comment
import re
from bs4 import BeautifulSoup
import requests
import dns.resolver
import smtplib


########## Missing Persons Code ##############
from .forms import MissingPersonForm, DiscussionForm
from .models import MissingPerson, DiscussionComment


def missing_persons(request):
    if request.method == "POST":
        missing_person_form = MissingPersonForm(request.POST, request.FILES)
        if missing_person_form.is_valid():
            missing_person_form.save()
            return redirect("mperson")
    else:
        missing_person_form = MissingPersonForm()

    if request.method == "POST":
        discussion_form = DiscussionForm(request.POST)
        if discussion_form.is_valid():
            discussion_form.save()
            return redirect("mperson")
    else:
        discussion_form = DiscussionForm()

    comments = DiscussionComment.objects.all().order_by("-timestamp")
    missing_persons = MissingPerson.objects.filter(is_approved=True)

    return render(
        request,
        "missing_persons.html",
        {
            "missing_person_form": missing_person_form,
            "discussion_form": discussion_form,
            "comments": comments,
            "missing_persons": missing_persons,
        },
    )


############## Missing persons code End ##################


############### Disaster and Crisis News Code Starts  ######################


def get_crisis_news():
    # Send a GET request to the URL
    url = "https://news.google.com/search?q=disaster%20in%20pakistan&hl=en-PK&gl=PK&ceid=PK%3Aen"
    response = requests.get(url)
    print("get_crisis_news")
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the articles on the page
    articles = soup.find_all("article")

    # Create a list to store the news articles
    news_list = []

    # Extract the title, link, and image of each article
    for article in articles:
        title = article.h3.text
        link = (
            "https://news.google.com/search?q=disaster%20in%20pakistan&hl=en-PK&gl=PK&ceid=PK%3Aen"
            + article.a["href"][1:]
        )
        image = article.find("img", class_="tvs3Id QwxBBf")
        if image:
            image_url = image["src"]
        else:
            image_url = None
        news = {"title": title, "link": link, "image_url": image_url}

        news_list.append(news)

    return news_list


def crisis_news(request):
    print("get_crisis_news")
    # Get the news articles using the get_crisis_news() function
    news_list = get_crisis_news()

    # Render the news articles on a webpage using the crisis_news.html template
    return render(request, "disaster.html", {"news_list": news_list})


# /////////////Above Scrapping Clases//////////////////


from .models import Notification, UserNotification


@login_required
def Dashboard(request):
    notifications = Notification.objects.filter(users=request.user)

    context = {
        "notifications": notifications,
    }
    return render(request, "indexDashboard.html", context)


@login_required
def submit_consent(request, notification_id):
    notification = Notification.objects.get(pk=notification_id)
    user_notification = UserNotification.objects.get(
        notification=notification, user=request.user
    )
    user_notification.consent = True
    user_notification.save()
    return redirect("indexDashboard")


##### Login Sign Up Code Starts Here ########


def validate_email(email):
    """
    Returns True if the given email address is valid, False otherwise
    """
    regex = r"^\S+@\S+\.\S+$"
    return bool(re.match(regex, email))


def validate_password(password):
    """
    Returns True if the given password meets the requirements, False otherwise
    """
    regex = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    return bool(re.match(regex, password))


def SignupPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Validate the password
        if not validate_password(password):
            error_message = "Password must contain only alphanumeric characters and be at least 8 characters long"
            return render(request, "signup.html", {"error_message": error_message})

        if len(username) < 3:
            error_message = "Username must be at least 3 characters long"
            return render(request, "signup.html", {"error_message": error_message})
        if not validate_password(password):
            error_message = "Password must be at least 8 characters long and contain at least one letter and one digit"
            return render(request, "signup.html", {"error_message": error_message})

        # Check if a user with the given username already exists
        if User.objects.filter(username=username).exists():
            error_message = "A user with that username already exists"
            return render(request, "signup.html", {"error_message": error_message})

        # Validate the email address
        if not validate_email(email):
            error_message = "Invalid email address"
            return render(request, "signup.html", {"error_message": error_message})

        # Check if the email address exists on a mail server
        domain = email.split("@")[1]
        try:
            records = dns.resolver.query(domain, "MX")
            mx_record = records[0].exchange.to_text()
            smtp = smtplib.SMTP()
            smtp.connect(mx_record)
            smtp.helo(smtp.local_hostname)
            smtp.mail("example@{}".format(domain))
            code, _ = smtp.rcpt(email)
            if code != 250:
                error_message = "Email address does not exist on a mail server"
                return render(request, "signup.html", {"error_message": error_message})
        except (
            dns.resolver.NoAnswer,
            dns.resolver.NoNameservers,
            dns.resolver.Timeout,
            smtplib.SMTPConnectError,
            smtplib.SMTPServerDisconnected,
        ):
            error_message = "Could not validate email address"
            return render(request, "signup.html", {"error_message": error_message})

        # Validate the password
        if not validate_password(password):
            error_message = "Password must contain only alphanumeric characters and be at least 8 characters long"
            return render(request, "signup.html", {"error_message": error_message})

        my_user = User.objects.create_user(username, email, password)
        my_user.save()
        return redirect("login")
    else:
        return render(request, "signup.html")


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        # Check that the username and password are at least 4 characters long
        if len(username) < 3 or len(password) < 8:
            error_message = "Username and password must be at least 4 characters long"
            return render(request, "login.html", {"error_message": error_message})

        if user is not None:
            login(request, user)
            return redirect("indexDashboard")
        else:
            error_message = "Invalid login credentials"
            return render(request, "login.html", {"error_message": error_message})
    else:
        return render(request, "login.html")


###### Login Sign Up Code Ends Here ######


###### Logout Code Starts #####


def LogoutPage(request):
    logout(request)
    return redirect("login")


#### Logout Code Ends Here ####


#### Contact Us/Feedback Form Code Here #####
def contact_us(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        mobileNo = request.POST["mobileNo"]
        textareafield = request.POST["textareafield"]
        my_type = ContactUs(
            name=name, email=email, mobileNo=mobileNo, textareafield=textareafield
        )
        my_type.save()
        return render(request, "contact_us.html")

    return render(request, "contact_us.html")


##### Contact Us/ Feedback Code Ends Here #######


################Stripe Payment Code Started###########################

import stripe

stripe.api_key = "sk_test_51N4675HXmzyEhldF2ZmOpUXUVLh9rUoiVXangt4kCE4ZmXmUD1Q6e0SFPyKss2kg4h4KusLrrQqdQZAOF2SRz18M00mnqv4I3w"


def stripePay(request):
    if request.method == "POST":
        amount = int(request.POST["amount"])
        # Create customer
        try:
            customer = stripe.Customer.create(
                email=request.POST.get("email"),
                name=request.POST.get("full_name"),
                description="Test donation",
                source=request.POST["stripeToken"],
            )

        except stripe.error.CardError as e:
            return HttpResponse(
                "<h1>There was an error charging your card:</h1>" + str(e)
            )

        except stripe.error.RateLimitError as e:
            # handle this e, which could be stripe related, or more generic
            return HttpResponse("<h1>Rate error!</h1>")

        except stripe.error.InvalidRequestError as e:
            return HttpResponse("<h1>Invalid requestor!</h1>")

        except stripe.error.AuthenticationError as e:
            return HttpResponse("<h1>Invalid API auth!</h1>")

        except stripe.error.StripeError as e:
            return HttpResponse("<h1>Stripe error!</h1>")

        except Exception as e:
            pass

        # Stripe charge
        charge = stripe.Charge.create(
            customer=customer,
            amount=int(amount) * 100,
            currency="usd",
            description="Test donation",
        )
        transRetrive = stripe.Charge.retrieve(
            charge["id"],
            api_key="sk_test_51N4675HXmzyEhldF2ZmOpUXUVLh9rUoiVXangt4kCE4ZmXmUD1Q6e0SFPyKss2kg4h4KusLrrQqdQZAOF2SRz18M00mnqv4I3w",
        )
        charge.save()  # Uses the same API Key.
        return redirect("pay_success/")

    return render(request, "Donationpay.html")


def paysuccess(request):
    return render(request, "success.html")


#############Stripe Payment Code Ended###########################

##### Save Adoption Form Started Here #####


def save_adoptionForm(request):
    if request.method == "POST":
        husb_name = request.POST["husb_name"]
        wife_name = request.POST["wife_name"]
        cnic = request.POST["cnic"]
        phone_no = request.POST["phone_no"]
        curr_address = request.POST["curr_address"]
        perm_address = request.POST["perm_address"]
        occup = request.POST["occup"]
        income = request.POST["income"]
        date_field = request.POST["date_field"]
        gender = request.POST["gender"]
        no_of_child = request.POST["no_of_child"]
        age = request.POST["age"]
        adopting_kids = request.POST["adopting_kids"]
        my_model = AdoptChild(
            husb_name=husb_name,
            wife_name=wife_name,
            cnic=cnic,
            phone_no=phone_no,
            curr_address=curr_address,
            perm_address=perm_address,
            occup=occup,
            income=income,
            date_field=date_field,
            gender=gender,
            no_of_child=no_of_child,
            age=age,
            adopting_kids=adopting_kids,
        )
        my_model.save()
        return render(request, "adoption.html")


def adoption_page(request):
    adopt_child_form = AdoptChildForm()

    context = {"form": adopt_child_form}
    return render(request, "adoption.html", context)


##### Save Adoption Form Ended Here #####


##### Simple Templates Code Starts Here #####


def index(request):
    achievement = Achievement.objects.first()

    context = {"achievement": achievement}
    return render(request, "index.html", context)


def about_us(request):
    return render(request, "about_us.html")


def blog_page(request):
    return render(request, "blog.html")


def news_page(request):
    return render(request, "disaster.html")


def donation_page(request):
    return render(request, "donation.html")


def services_page(request):
    return render(request, "services.html")


def gallery_page(request):
    return render(request, "gallery.html")


##### Simple Templates Code Ended Here #####
