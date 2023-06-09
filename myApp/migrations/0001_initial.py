# Generated by Django 4.1.5 on 2023-05-25 15:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Achievement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("experience_years", models.IntegerField(default=3)),
                ("happy_children", models.IntegerField(default=0)),
                ("food_drives", models.IntegerField(default=200)),
                ("funds_raised", models.IntegerField(default=2000000)),
            ],
        ),
        migrations.CreateModel(
            name="AdoptChild",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("husb_name", models.CharField(max_length=50, null=True)),
                ("wife_name", models.CharField(max_length=50, null=True)),
                ("cnic", models.CharField(max_length=14, null=True)),
                ("phone_no", models.CharField(max_length=14, null=True)),
                ("curr_address", models.CharField(max_length=100, null=True)),
                ("perm_address", models.CharField(max_length=100, null=True)),
                ("occup", models.CharField(max_length=14, null=True)),
                ("income", models.IntegerField(null=True)),
                ("date_field", models.DateField(null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")],
                        default="any",
                        max_length=10,
                    ),
                ),
                (
                    "no_of_child",
                    models.CharField(
                        choices=[("0", "0"), ("1", "1"), ("2", "2"), ("more", "More")],
                        default="any",
                        max_length=10,
                    ),
                ),
                (
                    "age",
                    models.CharField(
                        choices=[
                            ("below 30", "Below 30"),
                            ("30+", "30+"),
                            ("35+", "35+"),
                            ("40+", "40+"),
                            ("45+", "45+"),
                        ],
                        default="any",
                        max_length=10,
                    ),
                ),
                ("adopting_kids", models.CharField(max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="ContactUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, null=True)),
                ("email", models.CharField(max_length=50, null=True)),
                ("mobileNo", models.CharField(max_length=16, null=True)),
                ("textareafield", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="DiscussionComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("comment", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="MissingPerson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=100)),
                (
                    "age",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                ("gender", models.CharField(max_length=10)),
                ("date_of_birth", models.DateField()),
                ("last_location", models.CharField(max_length=100)),
                (
                    "height",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "weight",
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                ("hair_color", models.CharField(max_length=50)),
                ("distinguishing_marks", models.TextField()),
                ("reporter_name", models.CharField(max_length=100)),
                ("reporter_phone_number", models.CharField(max_length=20)),
                ("date_of_disappearance", models.DateField()),
                ("details", models.TextField()),
                ("photo", models.ImageField(upload_to="missing_person_photos/")),
                ("is_approved", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="MissingPersons",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=10)),
                ("hair_color", models.CharField(max_length=50)),
                ("eye_color", models.CharField(max_length=50)),
                ("height", models.CharField(max_length=10)),
                ("weight", models.CharField(max_length=10)),
                ("date_lost", models.DateField()),
                ("address", models.TextField()),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="missing_persons")),
                ("is_approved", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserNotification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("consent", models.BooleanField(default=False)),
                (
                    "notification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myApp.notification",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="notification",
            name="users",
            field=models.ManyToManyField(
                through="myApp.UserNotification", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
