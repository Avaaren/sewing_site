from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.NewsListView.as_view(), name='main_page'),
    
]