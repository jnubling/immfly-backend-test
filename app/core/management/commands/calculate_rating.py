"""
command to calculate the ratings of every Channel
"""
import csv
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db.models import Avg

from core.models import Channel, Content


class Command(BaseCommand):
    """
    command to iterate through all the contents in a channel
    or subchannel and calculate the average of the ratings
    """
    def handle(self, *args, **kwargs):
        channels = Channel.objects.all()

        ratings = []
        for channel in channels:
            rating = self._calculate_rating(channel)
            if rating is not None:
                ratings.append((channel.title, rating))

        ratings = sorted(ratings, key=lambda x: x[1], reverse=True)

        with open('ratings.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Channel Title', 'Average Rating'])
            for channel_title, rating in ratings:
                writer.writerow([channel_title, rating])

    def _calculate_rating(self, channel):
        """
        calculate the ratings of the channels considering the average of
        the ratings of the subchannels or contents of them
        """
        if channel.contents.exists():
            rating = Decimal(0)
            for content in channel.contents.all():
                rating += content.rating

            rating /= len(channel.contents.all())
            return round(rating, 2)

        elif channel.subchannels.exists():
            rating = Decimal(0)
            count = 0
            for subchannel in channel.subchannels.all():
                subchannel_rating = self._calculate_rating(subchannel)
                if subchannel_rating is not None:
                    rating += subchannel_rating
                    count += 1

            if count == 0:
                return None

            rating /= count
            return round(rating, 2)

        else:
            return None
