from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
        )
    
    age = models.PositiveSmallIntegerField(
        null=True,
        blank=True
        )
    bio = models.TextField(
        null=True,
        blank=True
        )
