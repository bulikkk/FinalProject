from .management.commands._private import (
    create_teams,
    create_players
)
from random import choice, randint

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .models import Player, Team, User
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
            return HttpResponseRedirect(reverse('create-team', kwargs={'user_pk': user.id}))
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
            return HttpResponseRedirect(reverse('actions', kwargs={'user_pk': user.id}))
        else:
            return render(request, 'app_football/login.html', ctx)


class LogoutUserView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('main'))


class CreateTeamView(View):

    def get(self, request, user_pk):
        form = CreateTeamForm()
        ctx = {'form': form}
        return render(request, 'app_football/create_team.html', ctx)

    def post(self, request, user_pk):
        form = CreateTeamForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            user = User.objects.get(pk=user_pk)
            team_name = form.cleaned_data['name']
            Team.objects.create(name=team_name, user=user, energy=10)

            create_teams()
            create_players(user_pk)
            return HttpResponseRedirect(reverse('team', kwargs={'user_pk': user.id}))
        else:
            return render(request, 'app_football/create_team.html', ctx)


class TeamView(View):

    def get(self, request, user_pk):
        user = User.objects.get(pk=user_pk)
        team = Team.objects.get(user=user)
        players = Player.objects.filter(team=team)
        ctx = {'players': players,
               'team': team}
        return render(request, 'app_football/team_view.html', ctx)


class PlayerView(View):

    def get(self, request, pk):
        player = Player.objects.get(pk=pk)
        ctx = {'player': player}
        return render(request, 'app_football/player_view.html', ctx)


class ActionsView(View):

    def get(self, request, user_pk):
        user = User.objects.get(pk=user_pk)
        team = Team.objects.get(user=user)
        ctx = {'team': team}
        return render(request, 'app_football/actions_view.html', ctx)


class TableView(View):

    def get(self, request):
        user = request.user
        teams = Team.objects.filter(user_id__gte=user.id, user_id__lte=(int(user.id)+15)).order_by('-points')

        ctx = {'teams': teams}
        return render(request, 'app_football/table_view.html', ctx)




class TrainingView(View):

    def get(self, request):
        user = request.user
        players = Player.objects.filter(team=user.team)
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
                return redirect(reverse('personal-training', kwargs={'player_pk': player_pk}))
        return render(request, 'app_football/personal_training.html', ctx)


class TeamTrainingView(View):

    def get(self, request):
        team = request.user.team
        players = team.player_set.all()
        ctx = {'players': players}
        return render(request, 'app_football/team_training.html', ctx)

    def post(self, request):
        team = request.user.team
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
                return redirect(reverse('team-training'))
        return render(request, 'app_football/personal_training.html', ctx)






class MatchView(View):

    def get(self, request):
        pass




















