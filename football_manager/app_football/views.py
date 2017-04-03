from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views import View
from .forms import RegisterUserForm


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
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'app_football/register_user_form.html', ctx)