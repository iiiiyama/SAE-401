from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
from . import models

class loginForm(ModelForm):
    class UserForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = models.login
        fields = ('username', 'password')
        labels = {
            'username' : _('Username'),
            'password' : forms.PasswordInput(),
        }

class accountForm(ModelForm):
    class Meta:
        model = models.account
        fields = ('nom', 'prenom', 'adresse', 'email','num_compte')
        labels = {
            'nom' : _('Nom'),
            'prenom' : _('Prenom') ,
            'adresse' : _('Adresse'),
            'email' : _('Email'),
            'num_compte' : _('Num_compte'),
        }
