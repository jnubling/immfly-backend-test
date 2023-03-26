"""
API models
"""
from django.conf import settings  # noqa
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
        return self.metadata


class Channel(models.Model):
    """Channel object"""
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='channels')
    # subchannel = models.ForeignKey(
    #     'self',
    #     on_delete=models.CASCADE,
    #     related_name='subchannels',
    #     null=True,
    #     blank=True,
    # )
    contents = models.ManyToManyField(
        Content,
        related_name='channels',
        blank=True,
    )
    subchannels = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='parent_channels'
    )

    def get_rating(self):
        """get the rating average of a channel's content"""
        if self.subchannels.exists():
            total_rating = 0
            for subchannel in self.subchannels.all():
                total_rating += subchannel.get_rating()
            return total_rating / self.subchannels.count()

        elif self.contents.exists():
            total_rating = 0
            for content in self.contents.all():
                if content.rating is not None:
                    total_rating += content.rating
            return total_rating / self.contents.count()

        else:
            return None

    def __str__(self):
        return self.title
