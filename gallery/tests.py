from django.test import TestCase
from .models import Image,Category, Location

# Create your tests h

class LocationTestClass(TestCase):

    def setUp(self):
        self.California = Location(location = 'California')

    def test_isinstance(self):
        self.assertTrue(isinstance(self.California,Location))
