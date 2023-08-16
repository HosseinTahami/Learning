from django.db import models


class Writer(models.Model):
    name = models.CharField(max_length=128)
    age = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} || {self.email}"
