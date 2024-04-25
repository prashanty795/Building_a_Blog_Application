from django.db import models

class Post(models.Model):
    """
    A model representing a blog post.
    """
    title = models.CharField(max_length=250)  # The title of the post
    slug = models.SlugField(max_length=250)  # A unique identifier for the post
    body = models.TextField()  # The body of the post

    def __str__(self):
        """
        Returns the title of the post as a string.
        """
        return self.title