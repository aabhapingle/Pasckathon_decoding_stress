
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.usersignup,name='register'),
    path('login', views.loginn,name='login'),
]
