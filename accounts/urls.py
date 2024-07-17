from django.urls import path, include
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.login_view, name='login'),
    ]