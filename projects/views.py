from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project
from main.views import PageTitleMixin

class ProjectListView(PageTitleMixin, ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'
    ordering = ['priority','-year']
    page_title = "Projects"

class ProjectDetailView(PageTitleMixin, DetailView):
    model = Project
    template_name = 'projects/projects-detail.html'
    context_object_name = 'project'

    def get_page_title(self, context):
        return context["project"].title