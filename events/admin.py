# events/admin.py
from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'datetime', 'location', 'enrollment_limit', 'created_at')
    list_filter = ('datetime', 'location')
    search_fields = ('title', 'description', 'location', 'author__username')
    ordering = ('-datetime',)
    fields = ('title', 'author', 'description', 'datetime', 'location', 'enrollment_limit', 'additional_details',
              'contact_information', 'event_banner', 'enrolled_users')
    readonly_fields = ('created_at',)


admin.site.register(Event, EventAdmin)
