from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    age = models.SmallIntegerField()

    def __str__(self):
        return f"{self.id} || {self.name}"

class Car(models.Model):
    brand = models.CharField(max_length=40)
    built_year = models.SmallIntegerField()
    name = models.name = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.brand} || {self.name}"