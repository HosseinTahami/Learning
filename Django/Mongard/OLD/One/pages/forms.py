from django import forms

from .models import Todo


class TodoCreateForm(forms.Form):

    title = forms.CharField(max_length=120, label="Todo Title")
    body = forms.CharField(label="Description", widget=forms.Textarea)


class TodoUpdateForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = (
            "title",
            "body",
        )
