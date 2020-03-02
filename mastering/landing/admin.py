from django.contrib import admin
from .models import NewsArticle

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text',]
    list_filter = ['created',]

    class Meta:
        ordering = ['-created',]
        verbose_name = 'article'
        verbose_name_plural = 'articles'