"""
We need to add here, so that we see our models/tables in the admin panel.
"""

from django.contrib import admin
from .models import Blog, Comment, Like
from accounts.admin_site import custom_admin_site


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date', 'author', 'status')
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('body',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')
    list_filter = ('post', 'user')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
