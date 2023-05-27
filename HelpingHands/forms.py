from django import forms

class SignUpForm(forms.Form):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    
    fullName = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    phoneNumber = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)


class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)