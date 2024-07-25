from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(default='default.png', blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

    @property
    def number_of_blogs_posted(self):
        Blog = apps.get_model('blogs', 'Blog')
        return Blog.objects.filter(author=self.user, status='published').count()
