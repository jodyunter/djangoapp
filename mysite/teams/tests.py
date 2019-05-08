"""Unit tests for Teams Models"""
from django.test import TestCase
from teams.models import Team
from teams.models import Game

# Create your tests here.

class GameTestCase(TestCase):
    """Unit Tests for Games Model"""    
    def setUp(self):
        team1 = Team.objects.create(name="Team 1", level=5)
        team2 = Team.objects.create(name="Team 2", level=5)

    def setUpGame(home_team, away_team)
        Game
