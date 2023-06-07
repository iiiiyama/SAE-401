from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class loginForm(ModelForm):
    class Meta:
        model = models.user_perso
        fields = ('nom', 'prenom', 'adresse', 'email','num_compte')
        labels = {
            'nom' : _('Nom'),
            'prenom' : _('Prenom') ,
            'adresse' : _('Adresse'),
            'email' : _('Email'),
            'num_compte' : _('Num_compte'),
        }
