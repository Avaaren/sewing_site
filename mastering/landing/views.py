from django.shortcuts import render
from .scraper import get_news_from_belta
from .models import NewsArticle
from django.views.generic import ListView


class NewsListView(ListView):
    model = NewsArticle
    paginate_by = 5
    context_object_name = 'news_list'
    template_name = 'landing/index.html'
    get_news_from_belta()