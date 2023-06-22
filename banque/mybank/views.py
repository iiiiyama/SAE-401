from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

from .forms import accountForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()

def compte(request):
    form = list(models.account.objects.all())
    return render(request,"compte.html",{"form": form})

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
        if request.POST == 'POST':
            rform = CustomUserCreationForm()
            if rform.is_valid():
                rform.save()
                return render(request,"compte.html", {"form": rform})
        else:
            rform = CustomUserCreationForm()
            return render(request, "register.html", {"form": rform})