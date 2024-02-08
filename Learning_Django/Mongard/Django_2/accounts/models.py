from django.db import models
from django.contrib.auth.models import User


class Relation(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followees')
    followee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers'
    )
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'{self.follower} --> {self.followee}')
