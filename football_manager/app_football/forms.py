from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

from .models import User



class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['username'].help_text = ""


    def clean(self):
        cleaned_data = super().clean()
        raw_password = cleaned_data['password']
        cleaned_data['password'] = make_password(raw_password)
        return cleaned_data


class AuthForm(forms.Form):
    login = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        """
        Metoda dorzuca do cleaned_data obiekt użytkowinika pod kluczem 'user'.
        """
        cleaned_data = super().clean()

        login = cleaned_data['login']
        password = cleaned_data['password']
        user = authenticate(username=login, password=password)

        if user is None:
            raise forms.ValidationError('Wrong username or password')

        cleaned_data['user'] = user
        return cleaned_data


class CreateTeamForm(forms.Form):
    name = forms.CharField(label='Team Name', max_length=64)






