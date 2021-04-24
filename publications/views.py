from django.shortcuts import render
from django.views.generic import ListView
from .models import Publication
from main.views import PageTitleMixin

# Create your views here.
class PublicationsListView(PageTitleMixin, ListView):
    model = Publication
    template_name = 'publications/publications.html'
    context_object_name = 'publications'
    ordering = ['kind','-year']
    page_title = "Publications"