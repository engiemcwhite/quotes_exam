# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils


# Create your models here.

import re,datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class BasicManager(models.Manager):
    def uservalidator(self,postData):
        errors = {}
        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
            errors["name"] = "Both first and last name must be 2 letters or more!"
        if any(not char.isalpha() for char in postData['first_name']) == True or any(not char.isalpha() for char in postData['last_name']) == True:
            errors["name2"] = "First and last name must only contain letters!"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Must use a valid email address!"
        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 characters long!"
        if postData['password'] != postData['password_confirmation']:
            errors['confirmation'] = "Password and Confirmation must match!"
        if datetime.datetime.now().isoformat() <= postData['birthday']:
            errors['birthday'] = "Begone, time traveler!"
        if postData['birthday'] == '':
            errors['birthday2'] = "Birthday field must be completely filled!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField(default=django.utils.timezone.now)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=BasicManager()

# Create your models here.
