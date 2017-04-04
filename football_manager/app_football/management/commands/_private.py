from faker import Factory
from random import randint

from football_manager.settings import *
from app_football.models import Player, Team, User



def create_teams_names():
    fake = Factory.create("en_GB")
    name = fake.last_name()
    return name + " FC"

def create_teams():
    fake = Factory.create("en_GB")
    for i in range(15):
        user = User.objects.create(username=(str(i) + str(randint(1, 10000)) + fake.first_name()))
        Team.objects.create(name=create_teams_names(), user=user, energy=0)

def create_name():
    fake = Factory.create("en_GB")
    first_name = fake.first_name()
    last_name = fake.last_name()
    return first_name, last_name


def create_players(user_pk):
    player_range = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    for team in Team.objects.filter(pk__gte=user_pk):
        for player in player_range:
            name = create_name()
            if player <= 3:
                att = randint(20, 30)
                deff = randint(50, 60)
                Player.objects.create(name=name[0], surname=name[1], position=1, attack=att, defence=deff, team=team)
            elif player <= 9:
                att = randint(30, 40)
                deff = randint(40, 50)
                Player.objects.create(name=name[0], surname=name[1], position=2, attack=att, defence=deff, team=team)
            elif player <= 15:
                att = randint(40, 50)
                deff = randint(30, 40)
                Player.objects.create(name=name[0], surname=name[1], position=3, attack=att, defence=deff, team=team)
            elif player <= 18:
                att = randint(50, 60)
                deff = randint(20, 30)
                Player.objects.create(name=name[0], surname=name[1], position=4, attack=att, defence=deff, team=team)



