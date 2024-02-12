# Django Imports

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User

# Project Imports

from .forms import UserChangeForm, UserCreationForm
from . import models


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm  # Create New User
    form = UserChangeForm  # Change User Data

    list_display = ['first_name', 'last_name',
                    'email', 'phone_number', 'is_admin']
    list_filter = ['is_admin']

    fieldsets = (
        ("User Information",
         {'fields':
          ('first_name', 'last_name', 'email', 'phone_number', 'password', 'birth_date',
           'address')
          }
         ),
        ("Permissions",
         {'fields':
          ('is_admin', 'is_active', 'last_login')
          }
         )
    )

    add_fieldsets = (
        ("User Information",
         {'fields':
          ('first_name', 'last_name', 'email', 'phone_number', 'password',
           'confirm_password', 'birth_date', 'address')
          }
         ),
    )

    search_fields = ['email', 'first_name', 'last_name', 'phone_number']
    ordering = ['first_name', 'last_name']
    filter_horizontal = ()


admin.site.unregister(Group)


@admin.register(models.OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'code']
