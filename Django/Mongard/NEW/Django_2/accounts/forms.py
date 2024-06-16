from django import forms


class RegistrationForm(forms.Form):

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    confirm_password = forms.CharField()
