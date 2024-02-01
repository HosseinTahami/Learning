from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Type
    # ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerFieldIntegerField()
    content_object = GenericForeignKey()
