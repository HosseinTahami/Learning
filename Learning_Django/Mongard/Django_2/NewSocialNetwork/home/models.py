from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.slug}'
    
    def get_absolute_url(self):
        return reverse('home:post_detail', args=(self.id, self.slug,))