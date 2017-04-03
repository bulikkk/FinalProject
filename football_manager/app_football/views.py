from .management.commands._private import (
    create_teams,
    create_players
)

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .models import Team, User
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
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'app_football/login.html', ctx)


class LogoutUserView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


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
            Team.objects.create(name=team_name, user=user)

            create_teams()
            create_players()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'app_football/create_team.html', ctx)























