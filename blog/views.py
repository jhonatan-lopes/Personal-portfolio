from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/posts-list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Journal"
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/posts-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Journal"
        return context