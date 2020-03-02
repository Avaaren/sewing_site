from django.contrib import admin

from .models import Comment, Topic

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'topic_text', 'created',)
    prepopulated_fields = {"slug": ("title",)}
    verbose_name = 'topic'
    verbose_name_plural = 'topics'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'topic', 'comment_text', 'created')
    verbose_name = 'comment'
    verbose_name_plural = 'comments'
