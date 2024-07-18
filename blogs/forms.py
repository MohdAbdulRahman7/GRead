from django import forms
from . import models
from django.utils.text import slugify
from .models import Blog


class CreateBlog(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title', 'body', 'slug', 'thumbnail']


        def clean_title(self):
            title = self.cleaned_data.get('title')
            slug = slugify(title)
            if Blog.objects.filter(slug=slug).exists():
                raise forms.ValidationError(
                    "A blog post with a similar title already exists. Please try a different title.")
            return title