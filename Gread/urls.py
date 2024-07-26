"""
URLS - FOR Base App - Gread.com
Urls - call the functions in views.py. Views functions contain logic regd. what to send as response.

"""

from django.contrib import admin
from django.urls import path, include  # here include is used to include other urls (from apps)
from . import views  # importing views.py from current directory(hence used '.')
from blogs import views as blogs_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  #for loading static files
from django.conf.urls.static import static  #For media Files
from django.conf import settings  #importing all vars and functions from settins.py file
from accounts.admin_site import custom_admin_site

urlpatterns = [
    path('', views.homepage, name='home'),
    # path('', blogs_views.blogs_list, name='home'),
    path('admin/', admin.site.urls),
    # path('admin/', custom_admin_site.urls),
    path('about/', views.about, name='about'),

    # We need to register urls for other apps here in the base urls.py, in order to access them
    path('blogs/', include('blogs.urls')),
    path('accounts/', include('accounts.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('events/', include('events.urls')),

    #     Test Urls
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
