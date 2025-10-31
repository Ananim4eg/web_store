from django.db import models

class Blog(models.Model):
    """Модель для блога"""

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog_preview/', verbose_name='Превью', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    publications_status = models.BooleanField(verbose_name="Признак публикации")
    count_views = models.IntegerField(null=True, blank=True, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['count_views']