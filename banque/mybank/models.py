from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=20,unique=True)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    username = 'username'

    objects = BaseUserManager()

    def __str__(self) -> str:
        return self.username

class account(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    #adresse = models.CharField(max_length=200)
    email = models.EmailField(max_length=30)
    nom_compte = models.CharField(max_length=20, unique=True, default='')
    num_compte = models.IntegerField(unique=True)
    
    def __str__(self) -> str:
        chaine = f"{self.prenom} {self.nom} à créé le compte {self.nom_compte}"
        return chaine
    
    def repertoire(self):
        return {"nom":self.nom, "prenom":self.prenom, "email":self.email, 'nom_compte':self.nom_compte, 'num_compte':self.num_compte}