from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class user_perso(AbstractUser):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    email = models.EmailField(max_length=30)
    num_compte = models.CharField(max_length=10, unique=True)
    
    def __str__(self) -> str:
        return self.username

#class PasswordResetForm()