from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'user@email.com',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '******',
                'class': 'form-control',
                'autocomplete': 'off', 'data-toggle': 'password'
            }
        )
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '******',
                'class': 'form-control'
            }
        )
    )

    # password.widget = forms.PasswordInput()

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This email already exists !')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError("This Username is already taken.")
        return username

    def clean(self):
        """clean() returns cleaned_data"""
        cd = super().clean()
        password = cd.get('password')
        confirm_password = cd.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords must match")


class UserLoginForm(forms.Form):
    authenticator = forms.CharField(
        label="Email or Username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email or Username'
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '******'
            }
        )
    )
