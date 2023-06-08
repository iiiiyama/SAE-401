from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

from .forms import loginForm
from . import models

def login(request):
    lform = loginForm(request.POST)
    if lform.is_valid():
        film = lform.save()
        return HttpResponseRedirect("/mybank/compte_perso/")
    else:
        return render(request,"mybank/login.html", {"form": lform})