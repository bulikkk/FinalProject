import names
from random import randint, choice

from football_manager.settings import *
from app_football.models import Player, Team, User, Match



def create_teams_names():
    name = names.get_last_name()
    return name + " FC"


def create_teams(user_id):
    for i in range(7):
        Team.objects.create(name=create_teams_names(), user=None, player_id=user_id)


def create_name():
    name = names.get_full_name(gender='male').split()
    return name


def create_players(user):
    player_range = [1,2,3,4,5,6,7,8,9,10,11]
    for team in Team.objects.filter(player_id=user.id):
        for player in player_range:
            name = create_name()
            if player <= 1:
                att = randint(20, 30)
                deff = randint(50, 60)
                Player.objects.create(name=name[0], surname=name[1], position=1, attack=att, defence=deff, team=team)
            elif player <= 6:
                att = randint(30, 40)
                deff = randint(40, 50)
                Player.objects.create(name=name[0], surname=name[1], position=2, attack=att, defence=deff, team=team)
            elif player <= 9:
                att = randint(40, 50)
                deff = randint(30, 40)
                Player.objects.create(name=name[0], surname=name[1], position=3, attack=att, defence=deff, team=team)
            elif player <= 11:
                att = randint(50, 60)
                deff = randint(20, 30)
                Player.objects.create(name=name[0], surname=name[1], position=4, attack=att, defence=deff, team=team)


def create_players_again(user):
    player_range = [1,2,3,4,5,6,7,8,9,10,11]
    for team in Team.objects.filter(player_id=user.id).filter(user=None):
        for player in player_range:
            name = create_name()
            if player <= 1:
                att = randint(20, 30)
                deff = randint(50, 60)
                Player.objects.create(name=name[0], surname=name[1], position=1, attack=att, defence=deff, team=team)
            elif player <= 6:
                att = randint(30, 40)
                deff = randint(40, 50)
                Player.objects.create(name=name[0], surname=name[1], position=2, attack=att, defence=deff, team=team)
            elif player <= 9:
                att = randint(40, 50)
                deff = randint(30, 40)
                Player.objects.create(name=name[0], surname=name[1], position=3, attack=att, defence=deff, team=team)
            elif player <= 11:
                att = randint(50, 60)
                deff = randint(20, 30)
                Player.objects.create(name=name[0], surname=name[1], position=4, attack=att, defence=deff, team=team)


def create_rounds(user_id):
    teams = Team.objects.filter(player_id=user_id)
    for home in teams:
        for away in teams:
            if home == away:
                continue
            round_no = 1
            index = 0
            matches = Match.objects.filter(player_id=user_id)
            if not matches:
                Match.objects.create(player_id=user_id, home_team=home, away_team=away, round_no=round_no)
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
                        Match.objects.create(player_id=user_id, home_team=home, away_team=away, round_no=round_no)
                        index += 1
                        break


def next_round(user):
    rounds = ((Match.objects.filter(home_team=user.team)) | (Match.objects.filter(away_team=user.team)))
    for round in rounds:
        if round.home_team_goals is None and round.away_team_goals is None:
            next = round.round_no
            match = round
            return next, match
    else:
        next = None
        match = None
        return next, match




def match_result(match):

    home_team_attack = 0
    home_team_defence = 0
    away_team_attack = 0
    away_team_defence = 0

    home_win = 25
    draw = 20
    away_win = 15

    home = match.home_team
    home_players = Player.objects.filter(team=home)
    for player in home_players:
        home_team_attack += player.attack
        home_team_defence += player.defence

    away = match.away_team
    away_players = Player.objects.filter(team=away)
    for player in away_players:
        away_team_attack += player.attack
        away_team_defence += player.defence

    if (home_team_attack > away_team_attack) and (home_team_defence > away_team_defence):
        home_win += 40
    elif (home_team_attack > away_team_attack) and (home_team_defence < away_team_defence):
        home_win += 20
        away_win += 20
    elif (home_team_attack > away_team_attack) and (home_team_defence == away_team_defence):
        home_win += 30
        away_win += 10
    elif (home_team_attack == away_team_attack) and (home_team_defence > away_team_defence):
        home_win += 30
        away_win += 10
    elif (home_team_attack == away_team_attack) and (home_team_defence < away_team_defence):
        home_win += 10
        away_win += 30
    elif (home_team_attack < away_team_attack) and (home_team_defence < away_team_defence):
        away_win += 40
    elif (home_team_attack < away_team_attack) and (home_team_defence > away_team_defence):
        home_win += 20
        away_win += 20
    elif (home_team_attack < away_team_attack) and (home_team_defence == away_team_defence):
        home_win += 10
        away_win += 30
    else:
        home_win += 20
        away_win += 20


    result = choice(range(1, 100))
    team_home_goals = 0
    team_away_goals = 0

    if result <= home_win:
        team_home_goals += choice(range(1, 10))
        team_away_goals += choice(range(0, team_home_goals))
    elif home_win < result <= (home_win + draw):
        team_home_goals += choice(range(0, 10))
        team_away_goals += team_home_goals
    elif result > (home_win + draw):
        team_away_goals += choice(range(1, 10))
        team_home_goals += choice(range(0, team_away_goals))

    match_result = [team_home_goals, team_away_goals]

    return match_result
























