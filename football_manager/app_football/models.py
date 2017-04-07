from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

POSITION_CHOICE = {
    1: 'GK',
    2: 'DF',
    3: 'MF',
    4: 'ST'
}


class User(AbstractUser):
    energy = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)], default=10)


class Team(models.Model):
    name = models.CharField(max_length=64)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default='null', blank=True)
    player_id = models.IntegerField()
    is_user_team = models.BooleanField(default=False)
    played = models.IntegerField(default=0, null=True)
    wins = models.IntegerField(default=0, null=True)
    draws = models.IntegerField(default=0, null=True)
    loses = models.IntegerField(default=0, null=True)
    goals_sum = models.IntegerField(default=0, null=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.name)


class Player(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    position = models.IntegerField(choices=POSITION_CHOICE.items())
    attack = models.IntegerField()
    defence = models.IntegerField()
    team = models.ForeignKey('Team')

    def __str__(self):
        return '{} {} | Position: {} | A: {} | D: {}'.format(self.name, self.surname, self.get_position_display(), self.attack, self.defence)

    @property
    def full_name(self):
        return "{} {}".format(self.name, self.surname)


class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name='home')
    away_team = models.ForeignKey(Team, related_name='away', null=True, default=None)
    round_no = models.IntegerField()
    home_team_goals = models.IntegerField(null=True, default=None)
    away_team_goals = models.IntegerField(null=True, default=None)

