from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
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

class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='username', min_length=5, max_length=30)  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def checkpswrd(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'], 
        )
        return user