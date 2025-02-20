from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm, EnrollmentForm

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('events:events_list')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})

def events_list(request):
    events = Event.objects.all().order_by('-datetime')
    return render(request, 'events/events_list.html', {'events': events})

