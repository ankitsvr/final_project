# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    full_name=models.CharField(max_length=255)
    user_phone=models.CharField(max_length=30)
    user_age=models.IntegerField(default=0)
    has_verified_mobile=models.BooleanField(default=False)
    created_on=models.DateTimeField(auto_now_add=True)

class UserModel(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=120)
    username=models.CharField(max_length=120)
    password=models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)