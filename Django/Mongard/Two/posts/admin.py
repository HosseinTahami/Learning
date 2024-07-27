from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ["title", "author", "created", "updated"]
    list_display_links = ["title"]
    list_filter = ["created", "updated"]
    search_fields = ["title", "slug"]
    prepopulated_fields = {"slug":("title",)}
    raw_id_fields = ["author"]

