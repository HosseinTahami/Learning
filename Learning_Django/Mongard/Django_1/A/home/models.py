from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    add_datetime = models.DateTimeField(auto_now_add=True)
    do_datetime = models.DateTimeField()
