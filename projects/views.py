from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'
    ordering = ['priority','-year']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Projects"
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/projects-detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Projects"
        return context