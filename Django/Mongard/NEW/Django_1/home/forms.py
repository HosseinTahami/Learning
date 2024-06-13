from django import forms
from .models import Todo


class CreateTodoForm(forms.Form):
    title = forms.CharField(label="Todo Title")
    body = forms.CharField(widget=forms.Textarea())


class UpdateTodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('title', 'body')
