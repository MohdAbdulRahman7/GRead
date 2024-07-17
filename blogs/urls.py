from django.urls import path
from . import views  # importing views.py from current directory(hence used '.')

app_name = 'blogs'

urlpatterns = [
    path('', views.blogs_list, name='blogs_list'),
   
]