from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

from .forms import accountForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import models
from django.contrib.auth import authenticate
from django.contrib import messages

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
        rform = CustomUserCreationForm(request)
        if rform.is_valid():
            rform.save()
            username = rform.cleaned_data['username'],
            password = rform.cleaned_data['password1'],
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.add_message(request, messages.success, 'utilisateur créé')
            return render(request,"compte.html")
            
    else:
        rform = UserCreationForm()
        return render(request, "register.html", {"form": rform})
    
def accounts(request):
    if request.method == "POST":
        form = accountForm(request.POST)
        if form.is_valid():
            account = form.save()
            return render(request, "compte.html", {"account": account})
        else:
            return render(request, "addaccount.html", {"form": form})
    else:
        form = accountForm()
        return render(request, "addaccount.html", {"form": form})

def affiche(request):
    liste = list(models.account.objects.all())
    return render(request,"compte.html",{"liste": liste})

def update(request, id):
    account = models.account.objects.get(pk=id)
    form = accountForm(account.repertoire())
    return render(request, "addaccount.html",{"form":form, "id":id})

def delete(request, id):
    account = models.account.objects.get(pk=id)
    account.delete()
    return HttpResponseRedirect("/compte")

def updatetraitement(request, id):
    form = accountForm(request.POST)
    if form.is_valid():
        account = form.save(commit=False)
        account.id = id
        account.save()
        return HttpResponseRedirect("/compte")
    else:
        return render(request, "addaccount.html", {"form": form, "id": id})
    
def traitement(request):
    form = accountForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/compte")
    else:
        return render(request,"addaccount.html", {"form": form})
    
def transfer(request):
    if request.method == 'POST':
        account_from = request.POST['account_from']
        account_to = request.POST['account_to']
        amount = request.POST['amount']

        account_from = models.account.objects.get(id)
        account_to = models.account.objects.get(id)

        if account_from.balance >= amount:
            
            account_from.balance -= amount
            account_to.balance += amount
            account_from.save()
            account_to.save()

            return HttpResponseRedirect("/opération")
    
    liste = list(models.account.objects.all())
    return render(request,"operations.html",{"liste": liste})