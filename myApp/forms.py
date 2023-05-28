from django import forms
from .models import Comment
from django.forms import RadioSelect

from .models import MissingPerson, DiscussionComment


class MissingPersonForm(forms.ModelForm):
    class Meta:
        model = MissingPerson
        fields = [
            "full_name",
            "age",
            "gender",
            "date_of_birth",
            "last_location",
            "height",
            "weight",
            "hair_color",
            "distinguishing_marks",
            "reporter_name",
            "reporter_phone_number",
            "date_of_disappearance",
            "details",
            "cast",
            "photo",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["full_name"].required = True
        self.fields["age"].required = True
        self.fields["gender"].required = True
        self.fields["date_of_birth"].required = True
        self.fields["last_location"].required = True
        self.fields["height"].required = True
        self.fields["weight"].required = True
        self.fields["hair_color"].required = True
        self.fields["distinguishing_marks"].required = True
        self.fields["reporter_name"].required = True
        self.fields["reporter_phone_number"].required = True
        self.fields["date_of_disappearance"].required = True
        self.fields["details"].required = True
        self.fields["cast"].required = True
        self.fields["photo"].required = True

    exclude = ["is_approved"]


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = DiscussionComment
        fields = ["name", "comment"]


class AdoptChildForm(forms.Form):
    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]
    CHILD_CHOICE = [("0", "0"), ("1", "1"), ("2", "2"), ("more", "More")]

    AGE_CHOICES = (
        ("below 30", "Below 30"),
        ("30+", "30+"),
        ("35+", "35+"),
        ("40+", "40+"),
        ("45+", "45+"),
    )

    husb_name = forms.CharField(
        label="Husband Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    wife_name = forms.CharField(
        label="Wife Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    cnic = forms.CharField(
        label="CNIC", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    phone_no = forms.CharField(
        label="Contact Number", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    curr_address = forms.CharField(
        label="Current Address", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    perm_address = forms.CharField(
        label="Permanent Address",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    occup = forms.CharField(
        label="Occupation/Business",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    income = forms.IntegerField(
        label="Monthly Income", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    date_field = forms.CharField(
        label="Date of Marriage",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        label="Gender",
        widget=forms.RadioSelect(
            attrs={"class": "ml-3 form-check-inline", "style": "padding-left: 10px;"}
        ),
    )
    no_of_child = forms.ChoiceField(
        choices=CHILD_CHOICE,
        label="How many childrens do you have",
        widget=forms.RadioSelect(
            attrs={"class": "ml-3 form-check-inline", "style": "padding-left: 10px;"}
        ),
    )
    age = forms.ChoiceField(
        choices=AGE_CHOICES,
        label="Age",
        widget=forms.RadioSelect(
            attrs={"class": "ml-3 form-check-inline", "style": "padding-left: 10px;"}
        ),
    )
    adopting_kids = forms.CharField(
        label="How many kids do you want to adopt",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "name",
            "text",
        )
