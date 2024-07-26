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


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    """
    Note: ForeignKey establishes a one-to-many relationship.
    Hence a single comment can have many replies, but each reply is related to exactly one parent comment.
    """
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

    @property
    def is_reply(self):
        return self.parent is not None


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    """
    Note: ForeignKey establishes a one-to-many relationship.
    Hence a single comment can have many replies, but each reply is related to exactly one parent comment.
    """
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

    @property
    def is_reply(self):
        return self.parent is not None


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    """
    Note: ForeignKey establishes a one-to-many relationship.
    Hence a single comment can have many replies, but each reply is related to exactly one parent comment.
    """
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

    @property
    def is_reply(self):
        return self.parent is not None


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    """
    Note: ForeignKey establishes a one-to-many relationship.
    Hence a single comment can have many replies, but each reply is related to exactly one parent comment.
    """
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

    @property
    def is_reply(self):
        return self.parent is not None