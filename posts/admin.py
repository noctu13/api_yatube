from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = '-пусто-'

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "post", "created", "author")
    search_fields = ("text",)
    list_filter = ("created",)
    empty_value_display = '-пусто-'

admin.site.register(Comment, CommentAdmin)