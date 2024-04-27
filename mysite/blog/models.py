from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    """
    A model representing a blog post.
    """
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PU', 'Published'
    title = models.CharField(max_length=250)  # The title of the post
    slug = models.SlugField(max_length=250)  # A unique identifier for the post
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()  # The body of the post
    publish = models.DateTimeField(default=timezone.now)  # When the post was published
    created = models.DateTimeField(auto_now_add=True)  # When this object was created (on save)
    updated = models.DateTimeField(auto_now=True)  # When this object was last updated (on save)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT) #  The current status of the post

    objects = models.Manager()    # The default manager.
    published = PublishedManager()  # Custom Manager, Used to filter posts by status.

    class Meta:
        ordering = [ '-publish'] # Orders by most recent posts first
        indexes =  [
            models.Index(fields=['-publish']), #  Orders by most recent posts first
        ]

    def __str__(self):
        """
        Returns the title of the post as a string.
        """
        return self.title