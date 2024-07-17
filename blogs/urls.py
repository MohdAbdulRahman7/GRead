from django.urls import path
from . import views  # importing views.py from current directory(hence used '.')

app_name = 'blogs'

urlpatterns = [
    path('', views.blogs_list, name='blogs_list'),
    # below regex: slug can be any character(word, number etc), also includes'-' and length is nolimit.
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
   
]