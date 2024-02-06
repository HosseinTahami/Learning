from django import forms
from .models import Todo


class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    create_at = forms.DateTimeField()
