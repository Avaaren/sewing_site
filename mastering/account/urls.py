from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('registration/', views.signup, name='registration'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]