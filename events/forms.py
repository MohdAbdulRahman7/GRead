from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'datetime', 'location', 'enrollment_limit', 'additional_details',
                  'contact_information', 'event_banner']

class EnrollmentForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput)