from django.shortcuts import render, HttpResponseRedirect, redirect

# Create your views here.

from .forms import loginForm, accountForm
from . import models
from django.shortcuts import render, HttpResponseRedirect

def compte(request):
    liste = list(models.account.objects.all())
    return render(request,"compte.html",{"form": accountForm})

def login(request):
    lform = loginForm(request.POST)
    if lform.is_valid():
        login = lform.save()
        return HttpResponseRedirect("/compte")
    else:
        return render(request,"login.html", {"form": loginForm})