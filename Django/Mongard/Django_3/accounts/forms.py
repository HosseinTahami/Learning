# Django Imports

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Project Imports

from .models import User


"""This form is for Admin Panel which you can Create Users inside it"""


class UserCreationForm(forms.ModelForm):

    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number',
                  'email', 'birth_date', 'address']

    def clean(self):
        cd = super().clean()
        password = cd.get('password')
        confirm_password = cd.get('confirm_password')
        if password and confirm_password and (password != confirm_password):
            raise ValidationError("Password dont match")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


"""This form is form Admin Panel which you can change Users credentials inside it"""


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="Change password with this <a href=\"../password/\">form</a>")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number',
                  'email', 'password', 'birth_date', 'address', 'last_login']


class UserRegisterForm(forms.Form):

    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'John'}))

    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Doe'}))

    phone_number = forms.CharField(label='Phone Number', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '09123456789'}))

    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'mail@email.com'}))

    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '******'}))


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField(label='OTP', widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "****"}))
