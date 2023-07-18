from django import forms
from .models import Todo
class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(label='Description', required=False)
    created = forms.DateTimeField()

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)