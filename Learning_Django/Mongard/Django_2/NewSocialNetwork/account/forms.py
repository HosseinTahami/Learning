from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='@Username',
        widget=forms.TextInput(
            attrs={
                'placeholder':'@username',
                'class':'form-control'
            }
        )
    )
    password = forms.CharField(        
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                'class':'form-control'
            }
        )
    )

class UserRegisterForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'placeholder':'@username',
                'class':'form-control'
                }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'placeholder':'YourMail@email.com',
                'class':'form-control'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control',
            }
        )
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Confirm Password',
                'class':'form-control'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError("This username already taken !")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This email is already used !')
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError("passwords Do not match !")