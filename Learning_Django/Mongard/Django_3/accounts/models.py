# Django Imports

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Project Imports

from .managers import UserManager

# Third-Party Imports

from random import randint


class User(AbstractBaseUser):
    username = models.CharField(
        max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=11, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class OTP(models.Model):

    phone_number = models.CharField(max_length=11, unique=True)
    code = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def code_creator(self):
        return randint(1000, 9999)

    def __str__(self) -> str:
        return f'{self.phone_number} || {self.code}'
