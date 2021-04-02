from django.contrib import admin
from django.utils.text import slugify
import tagulous.admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post

class PostAdmin(MarkdownxModelAdmin):
    list_display = ["title", "date_posted", "tags_list"]
    list_filter = ["tags"]
    prepopulated_fields = {'slug': ('title',)}
tagulous.admin.enhance(Post, PostAdmin)
tagulous.admin.register(Post, PostAdmin)

