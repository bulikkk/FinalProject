from faker import Factory
from random import randint

from football_manager.settings import *
from app_football.models import Player, Team, User, Match
from django.contrib.auth.models import User


def create_teams_names():
    fake = Factory.create("en_GB")
    name = fake.last_name()
    return name + " FC"

def create_teams(user_id):
    for i in range(7):
        Team.objects.create(name=create_teams_names(), user=None, player_id=user_id, energy=0)

def create_name():
    fake = Factory.create("en_GB")
    first_name = fake.first_name()
    last_name = fake.last_name()
    return first_name, last_name


def create_players(user):
    player_range = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    for team in Team.objects.filter(player_id=user.id):
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


def create_rounds(user_id):
    teams = Team.objects.filter(player_id=user_id)

    for team in teams:
        home = team
        for away in teams:
            away = away
            round_no = 1
            matches = Match.objects.all()
            index = 0
            if home == away:
                continue
            elif not matches:
                Match.objects.create(home_team=home, away_team=away, round_no=round_no)
                continue
            else:
                while index < 1:
                    for match in matches:
                            if match.home_team == home and match.round_no == round_no:
                                round_no += 1
                                break
                            elif match.away_team == home and match.round_no == round_no:
                                round_no += 1
                                break
                            elif match.away_team == away and match.round_no == round_no:
                                round_no += 1
                                break
                            elif match.home_team == away and match.round_no == round_no:
                                round_no += 1
                                break
                            else:
                                continue
                    else:
                        Match.objects.create(home_team=home, away_team=away, round_no=round_no)
                        index += 1
                        break
















    # teams.order_by("id")
    # rounds_no = (len(teams) - 1) * 2
    # for i in range(rounds_no):
    #     round_no = i
    #     for team in teams:
    #         matches = Match.objects.all()





















