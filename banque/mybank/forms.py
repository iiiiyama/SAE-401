from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from . import models

#class loginForm(ModelForm):
 #   class UserForm(forms.ModelForm):
  #      password = forms.CharField(widget=forms.PasswordInput)
   # class Meta:
    #    model = models.login
     #   fields = ('username', 'password')
      #  labels = {
       #     'username' : _('Username'),
        #    'password' : forms.PasswordInput(),
        #}

class accountForm(ModelForm):
    class Meta:
        model = models.account
        fields = ('nom', 'prenom', 'email', 'nom_compte', 'num_compte')
        labels = {
            'nom' : _('Nom'),
            'prenom' : _('Prenom') ,
            #'adresse' : _('Adresse'),
            'email' : _('Email'),
            'nom_compte' : _('Nom du compte'),
            'num_compte' : _('Numéro du compte'),
        }

class CustomUserCreationForm(UserCreationForm):
    model = models.CustomUser
    username = forms.CharField(label='Nom d utilisateur :', min_length=5, max_length=30)  
    password1 = forms.CharField(label='Nouveau mot de passe :', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='confirmer votre mot de passe :', widget=forms.PasswordInput)

    def checkpswrd(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 != password2:  
            raise ValidationError("pas le même mot de passe")  
        return password2  
  
    def save(self, commit = True):
        user = User.objects.create_user(  
            self.cleaned_data['username'],
            self.cleaned_data['password1'], 
        )
        return user
    
    