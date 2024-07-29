from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Relation(models.Model):

    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower} starts following {self.following}"