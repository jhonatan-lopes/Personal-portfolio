from django.contrib import admin
from .models import Project
import tagulous.admin

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "year", "categories_list", "technologies_list"]
    list_filter = ["year", "categories", "technologies"]
tagulous.admin.register(Project, ProjectAdmin)




# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ["abbreviated_name", "institution", "email"]

# class OwnerAdmin(admin.ModelAdmin):
#     list_display = ["abbreviated_name", "institution", "email"]

#     def has_add_permission(self, request, obj=None):
#         return False
    
#     def has_delete_permission(self, request, obj=None):
#         return False
