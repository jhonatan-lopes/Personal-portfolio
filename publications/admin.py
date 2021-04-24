from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Publication
import tagulous.admin


class PublicationAdmin(admin.ModelAdmin):
    list_display = ["title", "year", "authors_safe", "kind", "publisher"]
    list_filter = ["year", "kind"]

    def authors_safe(self, obj):
        # Returns authors field unescaped so it can be rendered properly in
        # admin page
        return mark_safe(obj.authors_list())
    authors_safe.short_description = "Authors"
tagulous.admin.register(Publication, PublicationAdmin)


