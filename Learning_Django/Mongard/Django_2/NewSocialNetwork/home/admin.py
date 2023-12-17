from django.contrib import admin
from .models import Post

"""admin.site.register(Post)"""

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'user', 'updated',)
    list_filter = ('created', 'user',)
    raw_id_fields = ('user',)
    prepopulated_fields = {'slug':('body','user',)}
    search_fields =  ('slug', 'body',)