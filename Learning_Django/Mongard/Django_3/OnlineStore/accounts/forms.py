from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("phone_number", "email", "full_name")

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if (
            cd["password"]
            and cd["confirm_password"]
            and cd["password"] != cd["confirm_password"]
        ):
            raise ValidationError("Passwords do not match.")
        return cd["confirm_password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="<a href=../password>Change Password</a>"
    )

    class Meta:
        model = User
        fields = ("phone_number", "email", "full_name", "password", "last_login")


class UserRegistrationForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(label="full name")
    phone = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()
