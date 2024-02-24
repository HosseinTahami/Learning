# Django Imports

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.SmallIntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'Name:{self.name}'
