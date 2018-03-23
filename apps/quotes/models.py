# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..registration.models import User
# Create your models here.
class QuoteManager(models.Manager):
    def quotevalidator(self,postData):
        errors = {}
        if len(postData['author']) < 4:
            errors["author"] = "Quote must be quoted by someone whose name is more than 3 characters long!"
        if len(postData['quote']) < 11:
            errors["quote"] = "Quote must be more than 10 characters long!"
        return errors

class Quote(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    postedby = models.ForeignKey(User, related_name="postedquotes")
    favoritedby = models.ManyToManyField(User,related_name="favquotes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=QuoteManager()



