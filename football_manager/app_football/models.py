from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

POSITION_CHOICE = {
    1: 'GK',
    2: 'DF',
    3: 'MF',
    4: 'ST'
}

class User(User):
    pass



class Team(models.Model):
    name = models.CharField(max_length=64)
    user = models.OneToOneField('User')
    energy = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)], null=True)

    def __str__(self):
        return self.name | self.user.username


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

