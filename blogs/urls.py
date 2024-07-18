"""
URLS - FOR Blogs App
Urls - call the functions in views.py. Views functions contain logic regd. what to send as response.

"""

from django.urls import path
from . import views  # importing views.py from current directory(hence used '.')

app_name = 'blogs'

urlpatterns = [
    path('', views.blogs_list, name='blogs_list'),
    path('create/', views.blog_create, name='blog_create'),
    path('drafts/', views.drafts_list, name='drafts_list'),
    path('load_draft/', views.load_draft, name='load_draft'),

    path('recently_viewed/', views.recently_viewed_blogs, name='recently_viewed_blogs'),
    # below regex: slug can be any character(word, number etc), also includes'-' and length is nolimit.
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),

]