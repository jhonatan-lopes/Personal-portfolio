from django.contrib import admin
from .models import Project
import tagulous.admin
from markdownx.admin import MarkdownxModelAdmin

class ProjectAdmin(MarkdownxModelAdmin):
    list_display = ["title", "year", "priority", "categories_list", "technologies_list"]
    list_filter = ["year", "categories", "technologies"]
tagulous.admin.enhance(Project, ProjectAdmin)
tagulous.admin.register(Project, ProjectAdmin)

