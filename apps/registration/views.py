# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from ..quotes.models import Quote
import bcrypt

#"date": strftime("%b %d, %Y", gmtime()),
  # the index function is called when root is visited
def index(request):
    return render(request,"registration/index.html")

def registration(request):
    errors = User.objects.uservalidator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/main')
    email = request.POST['email']
    if User.objects.filter(email=email).count() == 1:
        messages.error(request, "Email address is already in the database!")
        return redirect('/main')
    first = request.POST['first_name']
    last = request.POST['last_name']
    password = request.POST['password']
    bday = request.POST['birthday']
    print bday
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    User.objects.create(first_name = first, last_name = last, email = email, birthday = bday, password = hashed_pw)  
    request.session['name'] = first
    request.session['user_id'] = User.objects.get(email = email).id
    return redirect("/quotes")

def login(request):
    email = request.POST['mail']
    try:
        usermail = User.objects.get(email=email)
    except: 
        messages.warning(request, "Invalid login information!")
        return redirect('/main')
    passw = request.POST['pass']
    if bcrypt.checkpw(passw.encode(),usermail.password.encode()):
        request.session['name'] = usermail.first_name
        request.session['user_id'] = usermail.id
        return redirect("/quotes")
    else:
        messages.warning(request,"Invalid login information!")
        return redirect('/main')

def userpage(request,number):
    if 'user_id' not in request.session:
        return redirect('/main')
    context = {
        'user' : User.objects.get(id=number),
        'uploadedquotes' : Quote.objects.filter(postedby=number),
        'numquotes' : Quote.objects.filter(postedby=number).count()
    }
    return render(request,"registration/userpage.html", context)

def logout(request):
    request.session.flush()
    return redirect('/main')