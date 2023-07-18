from django import forms

class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(label='Description', required=False)
    created = forms.DateTimeField()