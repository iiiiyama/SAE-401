from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

from .forms import loginForm, accountForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()

def compte(request):
    liste = list(models.account.objects.all())
    return render(request,"compte.html",{"form": accountForm})

def login(request):
    if request.method == 'POST':
        lform = AuthenticationForm(request, data=request.POST)
        if lform.is_valid():
            user = lform.get_user()
            login(request, user)
            return HttpResponseRedirect("/compte")
    else:
        lform = AuthenticationForm()
        return render(request,"login.html", {"form": lform})

def register(request):
        if request.method == 'POST':
            rform = UserCreationForm(request.POST)
            if rform.is_valid():
                rform = rform.save()
                return render(request, "/login", {"form": rform})
        else:
            rform = UserCreationForm()
            return render(request, "register.html", {"form": rform})