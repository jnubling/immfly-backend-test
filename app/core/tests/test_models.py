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

    # def test_content(self):
    #     """test if creating a content is successful"""
    #     content = models.Content.objects.create(
    #         title='Sample Title',
    #         # file=<read doc file management>,
    #         metadata='Sample description here',
    #         rating=Decimal('7'),
    #         # channel=models.Channel.objects.create(
    #         #     title='Sample title here',
    #         #     language='English',
    #         #     # picture=<read docker file management>,
    #         # )
    #     )

    #     self.assertEqual(str(content), content.title)


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
    # def test_channel(self):
    #     """test if creating a channel is successful"""
    #     channel = models.Channel.objects.create(
    #         title='Sample title here',
    #         language='English',
    #         # picture=<read docker file management>,
    #     )

    #     self.assertEqual(str(channel), channel.title)

    def test_get_rating(self):
        """test if function get_rating is calculating right"""
        pass
