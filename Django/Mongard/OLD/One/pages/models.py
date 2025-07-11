from django.db import models
from django.urls import reverse
class Todo(models.Model):
    
    title = models.CharField(max_length=120)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("todo_detail", kwargs={"pk": self.pk})
    