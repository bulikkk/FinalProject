from .management.commands._private import (
    create_teams,
    create_players
)

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

    def get(self, request, user_pk):
        teams = Team.objects.filter(user_id__gte=user_pk, user_id__lte=(int(user_pk)+15)).order_by('points')

        ctx = {'teams': teams}
        return render(request, 'app_football/table_view.html', ctx)




class TrainingView(View):

    def get(self, request):
        pass





class MatchView(View):

    def get(self, request):
        pass




















