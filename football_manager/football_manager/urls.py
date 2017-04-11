"""football_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app_football.views import (
    ActionsView,
    CreateTeamView,
    EditPlayerView,
    GameView,
    IndexView,
    LeagueEndView,
    LoginUserView,
    LogoutUserView,
    LowEnergyView,
    MainView,
    MatchView,
    PersonalTrainingView,
    PlayerView,
    RegisterUserView,
    RoundView,
    ScheduleView,
    TableView,
    TeamView,
    TeamTrainingView,
    TrainingView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main$', MainView.as_view(), name='main'),
    url(r'^index$', IndexView.as_view(), name='index'),
    url(r'^low_energy$', LowEnergyView.as_view(), name='low-energy'),
    url(r'^register$', RegisterUserView.as_view(), name='register'),
    url(r'^login$', LoginUserView.as_view(), name='login'),
    url(r'^logout$', LogoutUserView.as_view(), name='logout'),
    url(r'^create_team$', CreateTeamView.as_view(), name='create-team'),
    url(r'^actions$', ActionsView.as_view(), name='actions'),
    url(r'^team$', TeamView.as_view(), name='team'),
    url(r'^edit_player/(?P<pk>(\d)+)$', EditPlayerView.as_view(), name='edit-player'),
    url(r'^training$', TrainingView.as_view(), name='training'),
    url(r'^personal_training/(?P<player_pk>(\d)+)$', PersonalTrainingView.as_view(), name='personal-training'),
    url(r'^team_training$', TeamTrainingView.as_view(), name='team-training'),
    url(r'^table$', TableView.as_view(), name='table'),
    url(r'^schedule$', ScheduleView.as_view(), name='schedule'),
    url(r'^round/(?P<round_no>(\d)+)$', RoundView.as_view(), name='round'),
    url(r'^match$', MatchView.as_view(), name='match'),
    url(r'^game$', GameView.as_view(), name='game'),
    url(r'^league_end$', LeagueEndView.as_view(), name='league-end'),


]
