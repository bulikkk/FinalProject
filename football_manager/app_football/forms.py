from django import forms
from django.forms import ModelForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

from .models import User, Player



class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['password'].widget.attrs['class'] = 'password-field'
        self.fields['username'].help_text = ""
        self.fields['username'].widget.attrs['class'] = 'login-field'
        self.fields['email'].widget.attrs['class'] = 'email-field'


    def clean(self):
        cleaned_data = super().clean()
        raw_password = cleaned_data['password']
        cleaned_data['password'] = make_password(raw_password)
        return cleaned_data


class AuthForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'class': 'login-field'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-field'}))

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
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'teamname-field'}))


class EditPlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'surname']






