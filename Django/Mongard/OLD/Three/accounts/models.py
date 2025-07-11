from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import UserManager

class User(AbstractBaseUser):

    username = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    is_active = models.BooleanField(default=True)
    age = models.SmallIntegerField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ["email", "first_name", "last_name"] # Create Super User
    EMAIL_FIELD = 'email'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
