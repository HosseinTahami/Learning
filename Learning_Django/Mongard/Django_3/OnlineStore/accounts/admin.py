from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('phone_number', 'email', 'full_name', 'is_admin')
    list_filter = ('is_admin', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'full_name', 'password')}),
        ('Permissions', {'fields': ('is_admin','is_superuser', 'is_active','last_login', 'groups', 'user_permissions')}),
    )
    
    add_fieldsets = (
        (None, {'fields':('phone_number', 'email', 'full_name', 'password', 'confirm_password')}),
        
        
    )
    
    search_fields = ('email', 'full_name')
    ordering = ('full_name',)
    filter_horizontal = ('groups', 'user_permissions',)
    
#admin.site.unregister(Group)
admin.site.register(User, UserAdmin)