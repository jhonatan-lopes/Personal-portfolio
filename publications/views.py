from django.shortcuts import render
from django.views.generic import ListView
from .models import Publication

# Create your views here.
class PublicationsListView(ListView):
    model = Publication
    template_name = 'publications.html'
    context_object_name = 'publications'
    ordering = ['type','-year']