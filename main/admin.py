from django.contrib import admin
from .models import Experience, Education, Expertise


class EducationAdmin(admin.ModelAdmin):
    list_display = ["title", "start_date", "end_date", "institution"]
admin.site.register(Education, EducationAdmin)

class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
admin.site.register(Expertise, ExpertiseAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["title", "start_date", "end_date", "company"]
admin.site.register(Experience, ExperienceAdmin)

