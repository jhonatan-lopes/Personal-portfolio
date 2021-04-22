from django.shortcuts import render
from django.views.generic import ListView
from .models import Publication

# Create your views here.
class PublicationsListView(ListView):
    model = Publication
    template_name = 'publications/publications.html'
    context_object_name = 'publications'
    ordering = ['kind','-year']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Publications"
        return context