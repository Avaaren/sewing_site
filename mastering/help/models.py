from django.db import models
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Topic(models.Model):
    author = models.ForeignKey(User,
                               related_name='topics',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(blank=True, null=True)
    topic_text = models.TextField(max_length=1024)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    
    class Meta:
        ordering =['-created']
        verbose_name = 'topic'
        verbose_name_plural = 'topics'
        
    def get_absolute_url(self):
        return reverse('help:topic_detail', args=[self.created.year,
                                                  self.created.month, self.created.day, self.slug])
    def __str__(self):
        return '{}'.format(self.title)

class Comment(models.Model):
    author = models.ForeignKey(User,
                               related_name='comments',
                               on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic,
                              related_name='comments',
                              on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ['-created']

    def __str__(self):
        return '{}'.format(self.comment_text)
