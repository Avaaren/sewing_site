from django.urls import path
from . import views

app_name = 'help'

urlpatterns = [
    path('forum/', views.TopicListView.as_view(), name='topic_list'),
    path('forum/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.TopicDetailView.as_view(), name='topic_detail'),
    path('forum/new/', views.TopicCreateView.as_view(), name='new_topic'),
    
]
