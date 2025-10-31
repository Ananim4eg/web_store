from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Blog


class BlogListView(ListView):
    """Контроллер для страницы блога"""
    model = Blog
    template_name = 'blog_main.html'
    context_object_name = 'article'
