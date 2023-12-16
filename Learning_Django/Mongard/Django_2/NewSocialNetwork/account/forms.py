from django import forms

class UserRegisterForm(forms.Form):
    username = forms.CharField(label='UserName',widget=forms.TextInput(attrs={'placeholder':'@username', 'class':'form-control'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder':'YourMail@email.com', 'class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control'}))

