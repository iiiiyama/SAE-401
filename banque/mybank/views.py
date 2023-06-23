from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

from .forms import accountForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import models
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from django.contrib import messages

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
    if request.method == "POST":
        rform = UserCreationForm(request.POST)
        if rform.is_valid():
            rform.save()
            username = rform.cleaned_data['username'],
            password1 = rform.cleaned_data['password1'],
            password2 = rform.cleaned_data['password2'],
            user = authenticate(username=username, password=password1)
            login(request, user)

            messages.add_message(request, messages.success, 'utilisateur créé')
            return render(request,"compte.html")

        if password1 != password2:  
            raise ValidationError("pas le même mot de passe")  
        return password2
    else:
        rform = UserCreationForm()
        return render(request, "register.html", {"form": rform})