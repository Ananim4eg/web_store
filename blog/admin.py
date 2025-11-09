from django.contrib import admin
from blog.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'preview', 'publications_status', 'count_views')
    list_filter = ('count_views', 'title',)
    search_fields = ('title', 'content')
