"""
tests for models
"""
from decimal import Decimal

from django.test import TestCase

from core.models import Content, Channel


class ContentTest(TestCase):
    """Test Content Model"""
    def setUp(self):
        """set up the object"""
        self.content = Content.objects.create(
            title='Sample Title',
            metadata='Sample Description Here',
            rating=Decimal('7'),
        )

    def test_content_creation(self):
        """test if creating a content is successful"""
        self.assertEqual(
            self.content.title, 'Sample Title'
        )
        self.assertEqual(
            self.content.metadata, 'Sample Description Here'
        )
        self.assertEqual(
            self.content.rating, Decimal('7')
        )


class ChannelTest(TestCase):
    """Test Channel Model"""
    def setUp(self) -> None:
        """set up the Channel object"""
        self.channel = Channel.objects.create(
            title='Channel',
            language='English',
            picture='channel1.jpg',
        )

    def test_channel_creation(self):
        """test if creating a channel is successful"""
        self.assertEqual(
            self.channel.title, 'Channel'
        )
        self.assertEqual(
            self.channel.language, 'English'
        )
        self.assertEqual(
            self.channel.picture, 'channel1.jpg'
        )

    def test_creating_channel_and_subchannel_with_content(self):
        """
        test if creating a subchannel in a channel
        with content(s) raise an error
        """
        pass

    def test_creating_channel_and_content_with_subchannel(self):
        """
        test if creating a content in a channel with
        subchannel(s) raise and error
        """
        pass

    def test_get_rating(self):
        """test if function get_rating is calculating right"""
        pass
