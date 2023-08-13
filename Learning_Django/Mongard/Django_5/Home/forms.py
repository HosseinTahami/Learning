from django import forms
from .models import Car


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
