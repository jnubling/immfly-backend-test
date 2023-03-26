"""
Test custom commands from Django management
"""
from django.test import TestCase

from decimal import Decimal

from core.models import Channel, Content
from core.management.commands.calculate_rating import Command


class CalculateRatingTest(TestCase):
    """test rating command"""
    pass
