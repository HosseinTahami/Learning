from django import forms


class CreateTodoForm(forms.Form):
    title = forms.CharField(label="Todo Title")
    body = forms.CharField(widget=forms.Textarea())
