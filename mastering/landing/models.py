from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=300, unique=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
       ordering = ['-created',]