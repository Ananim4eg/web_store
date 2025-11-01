from gc import get_objects

from django.db.models import F
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog


class BlogListView(ListView):
    """Контроллер для страницы блога"""
    model = Blog
    template_name = 'blog_main.html'
    context_object_name = 'article'

class BlogCreateView(CreateView):
    """Контроллер для страницы создания статьи"""
    model = Blog
    fields = ['title', 'content', 'preview', 'publications_status']
    template_name = 'blog_article_create.html'
    success_url = reverse_lazy('blog:blog_main')

class BlogDetailView(DetailView):
    """Контроллер для страницы с подробной информацией о статье"""
    model = Blog
    template_name = 'blog_article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.count_views += 1
        obj.save()
        return obj

class BlogUpdateView(UpdateView):
    """Контроллер для страницы изменения статьи"""
    model = Blog
    fields = ['title', 'content', 'preview', 'publications_status']
    template_name = 'blog_article_update.html'
    context_object_name = 'article'

    def get_success_url(self):
        return reverse_lazy('blog:article_detail', kwargs={'pk': self.object.pk})

class BlogDeleteView(DeleteView):
    """Контроллер для страницы удаления статьи"""
    model = Blog
    template_name = 'blog_article_delete.html'
    success_url = reverse_lazy('blog:blog_main')
