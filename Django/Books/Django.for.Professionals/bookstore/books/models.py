from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

import uuid

UserModel = get_user_model()


class Book(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to="covers/", blank=True)

    class Meta:
        permissions = [
            ("special_status", "Can read all books"),
        ]
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    



class Review(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    title = models.CharField(max_length=120)
    review = models.TextField()
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
