
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.welcome,name='welcome'),
    path('register', views.usersignup,name='register'),
    path('login', views.loginn,name='login'),
    path('answer', views.answer,name='answer'),
    path('logout', views.logoutt,name='logout'),
]
