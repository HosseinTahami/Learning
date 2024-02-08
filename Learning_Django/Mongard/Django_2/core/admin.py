from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'slug', 'updated']
    search_fields = ['slug']
    sortable_by = ['user']
    list_filter = ['updated', 'created']
    prepopulated_fields = {
        'slug': ['body'],
    }
    raw_id_fields = ['user']
