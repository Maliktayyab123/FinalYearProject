from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Comment(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Create your models here.
class AdoptChild(models.Model):
    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]
    CHILD_CHOICE = [("0", "0"), ("1", "1"), ("2", "2"), ("more", "More")]

    AGE_CHOICES = (
        ("below 30", "Below 30"),
        ("30+", "30+"),
        ("35+", "35+"),
        ("40+", "40+"),
        ("45+", "45+"),
    )

    husb_name = models.CharField(max_length=50, null=True)
    wife_name = models.CharField(max_length=50, null=True)
    cnic = models.CharField(max_length=14, null=True)
    phone_no = models.CharField(max_length=14, null=True)
    curr_address = models.CharField(max_length=100, null=True)
    perm_address = models.CharField(max_length=100, null=True)
    occup = models.CharField(max_length=14, null=True)
    income = models.IntegerField(null=True)
    date_field = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="any")
    no_of_child = models.CharField(max_length=10, choices=CHILD_CHOICE, default="any")
    age = models.CharField(max_length=10, choices=AGE_CHOICES, default="any")
    adopting_kids = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.husb_name


class ContactUs(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    mobileNo = models.CharField(max_length=16, null=True)
    textareafield = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User, through="UserNotification")


class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    consent = models.BooleanField(default=False)


class Achievement(models.Model):
    experience_years = models.IntegerField(default=3)
    happy_children = models.IntegerField(default=0)
    food_drives = models.IntegerField(default=200)
    funds_raised = models.IntegerField(default=2000000)

    def __str__(self):
        return "Achievement Numbers"


class MissingPerson(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    last_location = models.CharField(max_length=100)
    height = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    weight = models.FloatField(validators=[MinValueValidator(0)])
    hair_color = models.CharField(max_length=50)
    distinguishing_marks = models.TextField()
    reporter_name = models.CharField(max_length=100)
    reporter_phone_number = models.CharField(max_length=20)
    date_of_disappearance = models.DateField()
    details = models.TextField()
    photo = models.ImageField(upload_to="missing_person_photos/")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class DiscussionComment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MissingPersons(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    hair_color = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    date_lost = models.DateField()
    address = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="missing_persons")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
