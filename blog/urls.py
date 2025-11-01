from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_main'),
    path('article/create/', BlogCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/', BlogDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/edit/', BlogUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', BlogDeleteView.as_view(), name='article_delete'),
]