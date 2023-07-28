from django.contrib import admin
from .models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'body',)
    search_fields = ('user', 'body',)
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('user',)