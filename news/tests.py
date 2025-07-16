"""
Test suite for the news app.
"""
from django.test import TestCase

class BasicTestCase(TestCase):
    """
    Basic test to ensure the test framework is working.
    """
    def test_basic(self):
        self.assertEqual(1 + 1, 2)
