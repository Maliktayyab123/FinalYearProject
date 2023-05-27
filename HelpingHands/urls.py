"""HelpingHands URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from myApp import views
from myApp.admin import admin_site

admin.site.site_header = "Helping Hands"
admin.site.site_title = "Helping Hands"
admin.site.site_header = "Helping Hands"
admin.site.index_title = "Welcome to Helping Hands Dashboard"

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("about/", views.about_us, name="about"),
        path("", views.index, name="home"),
        path("contact_form/", views.contact_us, name="contact"),
        path("donation/f/", views.donation_page, name="donation"),
        path("missing_person/", views.missing_persons, name="mperson"),
        path("blogs/", views.blog_page, name="blog"),
        path("login/", views.LoginPage, name="login"),
        path("logout/", views.LogoutPage, name="logout"),
        path("join_us/", views.SignupPage, name="signup"),
        path("dashboard/", views.Dashboard, name="indexDashboard"),
        path(
            "submit-consent/<int:notification_id>/",
            views.submit_consent,
            name="submit_consent",
        ),
        path("services/", views.services_page, name="services"),
        path("gallery/", views.gallery_page, name="gallery"),
        path("adoption/", views.adoption_page, name="adoption"),
        path("save_adopt_form/", views.save_adoptionForm, name="save_adopt_form"),
        path("crisis-news/", views.crisis_news, name="crisis_news"),
        path("donation/", views.stripePay, name="donation_pay"),
        path("donation/pay_success/", views.paysuccess, name="success_page"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
