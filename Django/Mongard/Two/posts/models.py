from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.shortcuts import redirect

User = get_user_model()


class Post(models.Model):

    title = models.CharField(max_length=127)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts") 
    """
        related_name:

        post_set --> posts
        user.post_set.all() ---> user.posts.all()
    """

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"post_slug": self.slug})
        # return reverse("posts:post_detail", args=(self.slug,))

    class meta:
        ordering = ["created", "title"]

class Comment(models.Model):

    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    title = models.CharField(max_length=127)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name="comment_comments", blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} = {self.body[:20]}'
    