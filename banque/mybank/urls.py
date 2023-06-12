from django.urls import path
from . import views

urlpatterns = [
path('login', views.login),
path('compte', views.compte),
]