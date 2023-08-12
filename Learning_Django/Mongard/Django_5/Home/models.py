from django.db import models


class Building(models.Model):
    area = models.PositiveIntegerField()
    owner = models.CharField(max_length=50)
    pool = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.owner} || {self.area} m2"


class Car(models.Model):
    brand = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    build_year = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.brand} || {self.owner} || {self.build_year}"
