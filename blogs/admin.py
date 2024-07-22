"""
We need to add here, so that we see our models/tables in the admin panel.
"""

from django.contrib import admin
from .models import Blog, Member, Comment, Like, Event  # From models.py file import Blog class

# Register your models here.
admin.site.register(Blog)
admin.site.register(Member)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Event)
