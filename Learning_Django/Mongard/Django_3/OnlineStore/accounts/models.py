from django.db import models
from django.contrib.auth.models import AbstractBaseUser



class User(AbstractBaseUser):
    full_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=11,
        unique=True
        )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # This Field is called username but actually it is the field we authenticate our users with it !
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self) -> str:
        return f'Full Name: {self.full_name}, Phone Number: {self.phone_number}, Email: {self.email}'
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin