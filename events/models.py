from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetime = models.DateTimeField(null=True, blank=True)  # Allow null and blank values
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    enrollment_limit = models.PositiveIntegerField()
    enrolled_users = models.ManyToManyField(User, related_name='enrolled_events', blank=True)
    additional_details = models.TextField(blank=True)
    contact_information = models.CharField(max_length=255, blank=True)
    event_banner = models.ImageField(default='default.png', blank=True, null=True)

    def __str__(self):
        return self.title

    def is_full(self):
        return self.enrolled_users.count() >= self.enrollment_limit

    def shorter_description(self):
        return self.description[:90] + "..."
