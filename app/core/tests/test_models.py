"""
tests for models
"""
from decimal import Decimal

from django.test import TestCase

from core import models


class ModelTests(TestCase):
    """Test models"""
    def test_content(self):
        """test if creating a content is successful"""
        content = models.Content.objects.create(
            # file=<read doc file management>,
            metadata='Sample description here',
            rating=Decimal('7'),
            # channel=models.Channel.objects.create(
            #     title='Sample title here',
            #     language='English',
            #     # picture=<read docker file management>,
            # )
        )

        self.assertEqual(str(content), content.metadata)

    def test_channel(self):
        """test if creating a channel is successful"""
        channel = models.Channel.objects.create(
            title='Sample title here',
            language='English',
            # picture=<read docker file management>,
        )

        self.assertEqual(str(channel), channel.title)