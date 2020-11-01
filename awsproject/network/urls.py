from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.connection, name="index"),
    path('connection/', views.index, name="connection"),
]
