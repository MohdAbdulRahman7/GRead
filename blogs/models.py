from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)  # automatically populate date with this bool value
    thumbnail = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def shorter_body(self):
        return self.body[:70] + "..."