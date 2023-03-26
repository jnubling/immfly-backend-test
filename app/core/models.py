"""
API models
"""
from django.db import models
from django.core.files import File  # noqa


class Content(models.Model):
    """Content model object"""
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='contents')
    metadata = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=0)
    # channel = models.ForeignKey(
    #     'Channel',
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     )

    def __str__(self):
        return self.title


class Channel(models.Model):
    """Channel object"""
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='channels')
    contents = models.ManyToManyField(
        Content,
        # related_name='channels',
        blank=True,
    )
    subchannels = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='parent_channels'
    )
    parent_channel = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='subchannels',
        null=True,
        blank=True
        )

    # def get_rating(self):
    #     """
    #     Calculate the rating of the channel based on the
    #     ratings of its subchannels and/or contents.
    #     """
    #     if self.subchannels.exists():
    #         # Calculate the average rating of subchannels
    #         subchannel_ratings = [
    #             subchannel.get_rating() for subchannel in self.subchannels.all()
    #             ]
    #         rating = sum(subchannel_ratings) / len(subchannel_ratings)
    #     else:
    #         # Calculate the average rating of contents
    #         content_ratings = [
    #             content.rating for content in self.contents.all()
    #             ]
    #         if content_ratings:
    #             rating = sum(content_ratings) / len(content_ratings)
    #         else:
    #             rating = None
    #     return rating

    def __str__(self):
        return self.title
