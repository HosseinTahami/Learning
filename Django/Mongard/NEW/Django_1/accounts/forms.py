from django import forms


class UserRegistration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserLoginFrom(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
