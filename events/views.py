# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm, EnrollmentForm

def events_list(request):
    events = Event.objects.all().order_by('-datetime')
    return render(request, 'events/events_list.html', {'events': events})
