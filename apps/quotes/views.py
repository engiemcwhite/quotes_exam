# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Quote, User
import bcrypt

#"date": strftime("%b %d, %Y", gmtime()),
  # the index function is called when root is visited
def index(request):
    if 'user_id' not in request.session:
        return redirect('/main')

    id = request.session['user_id']
    context = {
        'quotables' : Quote.objects.exclude(favoritedby = id),
        'favorites' : Quote.objects.filter(favoritedby = id)
    }
    return render(request,"quotes/index.html",context)

def add(request):
    y = Quote.objects.get(id=request.POST['quoteid'])
    z = User.objects.get(id=request.session['user_id'])
    y.favoritedby.add(z)
    y.save()
    return redirect('/quotes')

def remove(request):
    y = Quote.objects.get(id=request.POST['quoteid'])
    z = User.objects.get(id=request.session['user_id'])
    y.favoritedby.remove(z)
    y.save()
    return redirect('/quotes')

def postquote(request):
    errors = Quote.objects.quotevalidator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/quotes')
    Quote.objects.create(author=request.POST['author'], text=request.POST['quote'], postedby = User.objects.get(id=request.session['user_id']))
    return redirect('/quotes')