from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib import admin

from .models import Relation, Profile

User = get_user_model()

@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ["follower", "following", "created"]
    raw_id_fields = ["follower", "following"]
    list_filter = ["created"]

class ProfileAdmin(admin.StackedInline):
    model = Profile
    can_delete = False

admin.site.unregister(User)

@admin.register(User)
class ExtendedUserAdmin(UserAdmin):
    inlines = (ProfileAdmin,)


