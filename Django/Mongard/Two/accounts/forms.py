from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()


class UserRegisterForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "example@email.com",
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "******"},
        )
    )    
    
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "******"},
        )
    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError(f'"{email}" is already registered.')
        return email

    def clean_username(self):
        username = self.cleaned_data["username"]
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError(f'"{username}" is already taken.')
        return username

    def clean(self):
        clean_data = super().clean()
        password = clean_data.get("password")
        confirm_password = clean_data.get("confirm_password")
        
        if password and confirm_password and password != confirm_password:
            raise ValidationError("password and confirm password must match.")


class UserLoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput)

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "******"},
        )
    )   

    