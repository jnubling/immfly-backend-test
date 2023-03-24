"""
API models
"""
from django.conf import settings
from django.db import models
from django.core.files import File

class Content(models.Model):
    """Content object"""
    file = models.FileField(upload_to='contents')
    metadata = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=0)
    channel = models.ForeignKey('Channel', on_delete=models.CASCADE)

    def __str__(self):
        return self.metadata


class Channel(models.Model):
    """Channel object"""
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='channels')

    def __str__(self):
        return self.title