from django import forms


class EnrollmentForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput)
