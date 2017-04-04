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
    IndexView,
    LoginUserView,
    LogoutUserView,
    MainView,
    MatchView,
    PlayerView,
    RegisterUserView,
    TableView,
    TeamView,
    TrainingView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main$', MainView.as_view(), name='main'),
    url(r'^index$', IndexView.as_view(), name='index'),
    url(r'^register$', RegisterUserView.as_view(), name='register'),
    url(r'^login$', LoginUserView.as_view(), name='login'),
    url(r'^logout$', LogoutUserView.as_view(), name='logout'),
    url(r'^create_team/(?P<user_pk>(\d)+)$', CreateTeamView.as_view(), name='create-team'),
    url(r'^actions/(?P<user_pk>(\d)+)$', ActionsView.as_view(), name='actions'),
    url(r'^team/(?P<user_pk>(\d)+)$', TeamView.as_view(), name='team'),
    url(r'^player/(?P<pk>(\d)+)$', PlayerView.as_view(), name='player'),
    url(r'^training/(?P<user_pk>(\d)+)$', TrainingView.as_view(), name='training'),
    url(r'^table/(?P<user_pk>(\d)+)$', TableView.as_view(), name='table'),
    url(r'^match/(?P<user_pk>(\d)+)$', MatchView.as_view(), name='match')

]
