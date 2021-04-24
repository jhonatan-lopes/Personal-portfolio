from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from main.views import PageTitleMixin

class PostListView(PageTitleMixin, ListView):
    model = Post
    template_name = 'blog/posts-list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10
    page_title = "Journal"

class PostDetailView(PageTitleMixin, DetailView):
    model = Post
    template_name = 'blog/posts-detail.html'
    context_object_name = 'post'

    def get_page_title(self, context):
        return context["post"].title