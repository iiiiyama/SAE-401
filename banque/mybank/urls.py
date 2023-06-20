from django.urls import path
from . import views

urlpatterns = [
path('login', views.login),
path('compte', views.compte),
path('register', views.register)
#path('accounts', views.accounts),
]