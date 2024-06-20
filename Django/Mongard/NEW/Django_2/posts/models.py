from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} | {self.slug}'

    def get_absolute_url(self):
        return reverse("posts:posts_detail", kwargs={"pk":self.pk, "post_slug":self.slug})
        return reverse("posts:post_details", args=(self.id, self.slug))