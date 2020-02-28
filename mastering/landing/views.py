from django.shortcuts import render
from .models import NewsArticle
from django.views.generic import ListView


class NewsListView(ListView):
    model = NewsArticle
    paginate_by = 10
    context_object_name = 'news_list'
    template_name = 'landing/index.html'
    