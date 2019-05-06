from django.test import TestCase
from teams.models import Team

# Create your tests here.

class GameTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="Team 1", level=5)
        Team.objects.create(name="Team 2", level=5)