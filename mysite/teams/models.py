#pylint:disable=E1101
"""Modles for teh Teams Application"""
from random import random
from django.db import models

class Team(models.Model):
    """Represents a team outside of any season"""
    name = models.CharField(max_length=200, unique=True)
    level = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)

    def __str__(self):
        return "%s %d %d %d %d" % (self.name, self.level, self.wins, self.loses, self.ties)

class Player(models.Model):
    """Represents a player outside of any season"""
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    skill = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)    

    def __str__(self):
        return "%s %s %d %d %d" % (self.team.name, self.name, self.skill, self.goals, self.assists)

class Game(models.Model):
    """Base implementaion of a game and how it should be played"""
    home_team = models.ForeignKey(Team, null=False, related_name='home_team',
                                  on_delete=models.PROTECT)
    away_team = models.ForeignKey(Team, null=False, related_name='away_team',
                                  on_delete=models.PROTECT)
    year = models.IntegerField()
    day = models.IntegerField()
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)

    def __str__(self):     
        return "%d-%d. %s : %d - %d : %s" % (self.year, self.day, self.homeTeam.name, self.homeScore, self.awayScore, self.awayTeam.name)

            
    def play(self):
        """Method to play games"""
        difference = self.home_team.level - self.away_team.level
        self.home_score = random.randint(0, self.home_team.level + difference)
        self.away_score = random.randint(0, self.away_team.level - difference)
    