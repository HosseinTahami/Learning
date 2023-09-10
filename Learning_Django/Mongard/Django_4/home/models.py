from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    age = models.SmallIntegerField()

    def __str__(self):
        return f"{self.id} || {self.name}"
