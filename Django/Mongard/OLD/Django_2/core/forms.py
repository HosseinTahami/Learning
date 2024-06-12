from django import forms
from .models import Post, Comment


class PostCreateUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body']


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control col-md-9', 'placeholder': 'Write your Comment'})
        }
        labels = {
            'body': 'New Comment',
        }


class ReplyCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control col-md-9', 'placeholder': 'Reply the Comment'})
        }
        labels = {
            'body': 'Reply Comment',
        }
