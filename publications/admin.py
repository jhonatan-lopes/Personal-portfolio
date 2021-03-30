from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Publication


class PublicationAdmin(admin.ModelAdmin):
    list_display = ["title", "year", "authors_safe", "kind", "publisher"]

    def authors_safe(self, obj):
        # Returns authors field unescaped so it can be rendered properly in
        # admin page
        return mark_safe(obj.authors)
    authors_safe.short_description = "Authors"

# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ["abbreviated_name", "institution", "email"]

# class OwnerAdmin(admin.ModelAdmin):
#     list_display = ["abbreviated_name", "institution", "email"]

#     def has_add_permission(self, request, obj=None):
#         return False
    
#     def has_delete_permission(self, request, obj=None):
#         return False

# Register your models here.
admin.site.register(Publication, PublicationAdmin)
# admin.site.register(Author, AuthorAdmin)
# admin.site.register(PublicationAuthor)
# admin.site.register(Owner, OwnerAdmin)

