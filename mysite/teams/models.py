#pylint:disable=E1101
from django.db import models
from random import random

class Team(models.Model):
    name = models.CharField(max_length=200,unique=True)
    level = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)

    def __str__(self):
        return "%s %d %d %d %d" % (self.name, self.level, self.wins, self.loses, self.ties)

class Player(models.Model):
    team = models.ForeignKey(Team,null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    skill = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)    

    def __str__(self):        
        return "%s %s %d %d %d" % (self.team.name, self.name, self.skill,  self.goals, self.assists)

class Game(models.Model):
    homeTeam = models.ForeignKey(Team,null=False, related_name='home_team', on_delete=models.PROTECT)
    awayTeam = models.ForeignKey(Team,null=False, related_name='away_team', on_delete=models.PROTECT)
    year = models.IntegerField()
    day = models.IntegerField()    
    homeScore  = models.IntegerField(default=0)
    awayScore = models.IntegerField(default=0)

    def __str__(self):        
        return "%d-%d %s %d - %d %s" % (self.year, self.day, self.homeTeam.name, self.homeScore, self.awayScore, self.awayTeam.name)

            
    def play(self):                         
        difference = self.homeTeam.level - self.awayTeam.level
        self.homeScore = random.randint(0, self.homeTeam.level + difference)
        self.awayScore = random.randint(0, self.awayTeam.level - difference)
    