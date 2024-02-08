from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title} || {self.user}'

    def get_absolute_url(self):
        return reverse('core:post_detail', args=(self.id, self.slug))


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    reply_to = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)
    body = models.TextField()
    is_reply = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user}||{self.body[:10]}||{self.post.title}'
