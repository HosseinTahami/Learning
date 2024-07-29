from django.contrib import admin

from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ["title", "author", "created", "updated"]
    list_display_links = ["title"]
    list_filter = ["created", "updated"]
    search_fields = ["title", "slug"]
    prepopulated_fields = {"slug":("title",)}
    raw_id_fields = ["author"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["title", "commenter", "created", "is_reply", "post"]
    raw_id_fields = ["post", "reply", "commenter"]
