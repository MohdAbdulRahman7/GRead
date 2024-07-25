from django import forms
from . import models
from django.utils.text import slugify
from .models import Blog, Comment


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4}),
        }