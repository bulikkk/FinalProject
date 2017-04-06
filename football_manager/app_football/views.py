from .management.commands._private import (
    create_teams,
    create_players,
    create_rounds,
    match_result,
    next_round,
)
from random import choice, randint

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .models import Player, Team, Match
from django.views import View
from .forms import (
    AuthForm,
    CreateTeamForm,
    RegisterUserForm
)
from django.contrib.auth import get_user_model, authenticate, login, logout


class IndexView(View):

    def get(self, request):
        return render(request, 'app_football/index.html', {})


class MainView(View):

    def get(self, request):
        return render(request, 'app_football/main.html', {})


class LowEnergyView(View):

    def get(self, request):
        return render(request, 'app_football/low_energy.html', {})


class RegisterUserView(View):
    def get(self, request):
        form = RegisterUserForm()
        ctx = {'form': form}
        return render(request, 'app_football/register_user_form.html', ctx)

    def post(self, request):
        form = RegisterUserForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('create-team'))
        else:
            return render(request, 'app_football/register_user_form.html', ctx)


class LoginUserView(View):

    def get(self, request):
        form = AuthForm()
        ctx = {'form': form}
        return render(request, 'app_football/login.html', ctx)

    def post(self, request):
        form = AuthForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return HttpResponseRedirect(reverse('actions'))
        else:
            return render(request, 'app_football/login.html', ctx)


class LogoutUserView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('main'))


class CreateTeamView(View):

    def get(self, request):
        form = CreateTeamForm()
        ctx = {'form': form}
        return render(request, 'app_football/create_team.html', ctx)

    def post(self, request):
        form = CreateTeamForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            user = request.user
            user_id = request.user.id
            team_name = form.cleaned_data['name']
            Team.objects.create(name=team_name, user=user, player_id=user_id, energy=10, is_user_team=True)

            create_teams(user_id)
            create_players(user)
            create_rounds(user_id)
            return HttpResponseRedirect(reverse('actions'))
        else:
            return render(request, 'app_football/create_team.html', ctx)


class TeamView(View):

    def get(self, request):
        team = Team.objects.get(user=request.user)
        players = Player.objects.filter(team=team)
        ctx = {'players': players}
        return render(request, 'app_football/team_view.html', ctx)


class PlayerView(View):

    def get(self, request, pk):
        player = Player.objects.get(pk=pk)
        ctx = {'player': player}
        return render(request, 'app_football/player_view.html', ctx)


class ActionsView(View):

    def get(self, request):
        team = Team.objects.get(user=request.user)
        ctx = {'team': team}
        return render(request, 'app_football/actions_view.html', ctx)


class TableView(View):

    def get(self, request):
        user = request.user
        teams = Team.objects.filter(player_id=user.id).order_by('-points')

        ctx = {'teams': teams}
        return render(request, 'app_football/table_view.html', ctx)




class TrainingView(View):

    def get(self, request):
        team = Team.objects.get(user=request.user)
        players = Player.objects.filter(team=team)
        ctx = {'players': players}
        return render(request, 'app_football/training_view.html', ctx)


class PersonalTrainingView(View):

    def get(self, request, player_pk):
        player = Player.objects.get(pk=player_pk)
        ctx = {'player': player}
        return render(request, 'app_football/personal_training.html', ctx)

    def post(self, request, player_pk):
        player = Player.objects.get(pk=player_pk)
        team = player.team
        ctx = {'player': player}
        if request.POST.get("train_att"):
            if team.energy < 2:
                return redirect(reverse('low-energy'))
            else:
                player.attack += 2
                player.save()
                team.energy -= 2
                team.save()
                return redirect(reverse('personal-training', kwargs={'player_pk': player_pk}))
        elif request.POST.get("train_def"):
            if team.energy < 2:
                return redirect(reverse('low-energy'))
            else:
                player.defence += 2
                player.save()
                team.energy -= 2
                team.save()
                return render(request, 'app_football/personal_training.html', ctx)
        return render(request, 'app_football/personal_training.html', ctx)


class TeamTrainingView(View):

    def get(self, request):
        team = Team.objects.get(user=request.user, is_user_team=True)
        players = team.player_set.all()
        ctx = {'players': players}
        return render(request, 'app_football/team_training.html', ctx)

    def post(self, request):
        team = Team.objects.get(user=request.user, is_user_team=True)
        players = team.player_set.all()
        ctx = {'players': players}
        if request.POST.get("team_train"):
            if team.energy < 4:
                return redirect(reverse('low-energy'))
            else:
                team.energy -= 4
                team.save()
                for i in range(0, 3):
                    player = choice(players)
                    atr = randint(0, 1)
                    if atr == 0:
                        player.attack += 2
                        player.save()
                    elif atr == 1:
                        player.defence += 2
                        player.save()
                return render(request, 'app_football/team_training.html', ctx)
        return render(request, 'app_football/personal_training.html', ctx)


class ScheduleView(View):

    def get(self, request):
        teams = Team.objects.filter(player_id=request.user.id)
        rounds_no = ((len(teams) - 1) * 2)
        rounds = []
        for i in range(1, rounds_no + 1):
            rounds.append(i)
        ctx = {'rounds': rounds}
        return render(request, 'app_football/schedule.html', ctx)


class RoundView(View):

    def get(self, request, round_no):
        matches = Match.objects.filter(round_no=round_no).order_by('home_team')
        ctx = {'matches': matches,
               'round_no': round_no}
        return render(request, 'app_football/round.html', ctx)


class MatchView(View):

    def get(self, request):
        user = request.user
        next_match = next_round(user)[0]
        matches = Match.objects.filter(round_no=next_match)
        ctx = {'matches': matches}
        return render(request, 'app_football/match.html', ctx)


class GameView(View):

    def get(self, request):
        user = request.user
        match = next_round(user)[1]
        home = match.home_team
        home_players = Player.objects.filter(team=home)
        away = match.away_team
        away_players = Player.objects.filter(team=away)
        ctx = {'match': match,
               'home': home,
               'home_players': home_players,
               'away': away,
               'away_players': away_players}
        return render(request, 'app_football/game.html', ctx)

    def post(self, request):
        user = request.user
        team = Team.objects.get(user=user)
        round_no = next_round(user)[0]
        match = next_round(user)[1]
        result = match_result(match)
        match.home_team_goals = result[0]
        match.away_team_goals = result[1]
        match.save()
        team.energy -= 6
        team.save()
        if result[0] > result[1]:
            match.home_team.wins += 1
            match.home_team.points += 3
            match.away_team.loses += 1
            match.home_team.save()
            match.away_team.save()
        elif result[0] < result[1]:
            match.home_team.loses += 1
            match.away_team.points += 3
            match.away_team.wins += 1
            match.home_team.save()
            match.away_team.save()
        elif result[0] == result[1]:
            match.home_team.draws += 1
            match.home_team.points += 1
            match.away_team.points += 1
            match.away_team.draws += 1
            match.home_team.save()
            match.away_team.save()
        return redirect(reverse('round', kwargs={'round_no': round_no}))






















