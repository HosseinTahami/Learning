from django import forms

from .models import Post, Comment


class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            "title",
            "body",
        )


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            "title",
            "body",
        )


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = (
            "title",
            "body",
        )


class CommentReplyForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = (
            "title",
            "body",
        )
