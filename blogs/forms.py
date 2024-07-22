from django import forms
from . import models
from django.utils.text import slugify
<<<<<<< HEAD
from .models import Blog, Comment
=======
from .models import Blog
>>>>>>> c39e2c1356dfd382015cc6868217db3fc95ea0f2


class CommentForm(forms.ModelForm):
    class Meta:
<<<<<<< HEAD
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4}),
        }
=======
        model = models.Blog
        fields = ['title', 'body', 'slug', 'thumbnail']


        def clean_title(self):
            title = self.cleaned_data.get('title')
            slug = slugify(title)
            if Blog.objects.filter(slug=slug).exists():
                raise forms.ValidationError(
                    "A blog post with a similar title already exists. Please try a different title.")
            return title
>>>>>>> c39e2c1356dfd382015cc6868217db3fc95ea0f2
