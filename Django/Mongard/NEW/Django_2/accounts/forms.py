from .models import User
from django.core.exceptions import ValidationError
from django import forms


class RegistrationForm(forms.Form):

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Username"
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "example@email.com"
            }

        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "*******",
            }
        )
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "*******",
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError("This Email has already been taken !")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError("This Username has already been taken !")
        return username

    def clean(self):
        cd = super().clean()
        pw1 = cd.get('password')
        pw2 = cd.get('confirm_password')
        if pw1 and pw2 and pw1 != pw2:
            raise ValidationError("Password & Confirm Password do not match !")


class LoginForm(forms.Form):

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Username"
            }
        )
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "*******",
            }
        )
    )
