from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ppl/', views.ppl, name="ppl"),
    path('connection/', views.connection, name="connection"),
]
