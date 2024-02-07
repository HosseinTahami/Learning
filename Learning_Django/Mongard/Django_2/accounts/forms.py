from django import forms


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
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'your password',
                'class': 'form-control'
            }
        )
    )

    # password.widget = forms.PasswordInput()
