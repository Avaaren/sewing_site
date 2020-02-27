from django.shortcuts import render
from .scraper import get_news_from_belta

def main_page(request):
    news_list = get_news_from_belta()

    return render(request, 'landing/index.html', {'news_list': news_list})
