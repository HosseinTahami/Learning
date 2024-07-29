from django.contrib import admin

from .models import Relation


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ["follower", "following", "created"]
    raw_id_fields = ["follower", "following"]
    list_filter = ["created"]
    