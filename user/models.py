from django.db import models
from django.contrib.auth.models import User
# from django.core.files.storage import FileSystemStorage
# import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(default='example@gmail.com')