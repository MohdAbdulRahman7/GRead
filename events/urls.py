# events/urls.py
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('add_event/', views.add_event, name='add_event'),
    path('enroll_event/', views.enroll_event, name='enroll_event'),
    path('unenroll_event/', views.unenroll_event, name='unenroll_event'),
    path('my_events/', views.my_events, name='my_events'),
    path('', views.events_list, name='events_list'),
]
