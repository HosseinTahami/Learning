from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(forms.Form):
    username = forms.CharField(label='UserName',widget=forms.TextInput(attrs={'placeholder':'@username', 'class':'form-control'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder':'YourMail@email.com', 'class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control'}))

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
    
