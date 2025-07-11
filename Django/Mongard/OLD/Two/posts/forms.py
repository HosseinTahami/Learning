from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Comment, Like


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


class LikeAdminForm(forms.ModelForm):

    class Meta:
        model = Like
        fields = (
            "liker",
            "post",
        )

    def clean(self):
        clean_data = super().clean()
        post = clean_data.get("post")
        liker = clean_data.get("liker")
        like = Like.objects.filter(post=post, liker=liker).exists()
        if like:
            raise ValidationError("This User Already Liked This Post.")

class PostSearchForm(forms.Form):
    search = forms.CharField()