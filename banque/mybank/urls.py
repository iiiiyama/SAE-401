from django.urls import path
from . import views

urlpatterns = [
path('login', views.login),
path('compte', views.affiche),
path('register', views.register),
path('addaccount', views.accounts),
path('affiche/', views.affiche),
path('affiche/<int:id>/',views.affiche),
path('update/<int:id>/',views.update),
path('updatetraitement/<int:id>/', views.updatetraitement),
path('traitement/', views.traitement),
path('delete/<int:id>/', views.delete),
path('operations/', views.operation_affiche),
path('virement_int', views.virement_int)
]