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
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "*******",
            }
        )
    )
