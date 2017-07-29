# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from datetime import datetime
from app1.forms import SignUpform
from django.contrib.auth.hashers import make password
from app1.models import Usermodel1
# Create your views here.
def signup_view(request):
    if request.method=='GET':
       signup_form=SignUpform()
       template_name='signup.html'

        #display form
        #post process form
    elif request.method=='POST':
          signup_form=SignUpform(request.POST)
          #validate the form data
           if form.is_valid():

              #data is valid succefully

              username=signup_form.cleaned_data['username']
              name=signup_form.cleaned_data['name']
              email=signup_form.cleaned_data['email']
              passsword=signup_form.cleaned_data['password']
              user = Usermodel1(name=name, password=make_password(password), email=email, username=username)
              user.save()
              template_name='success.html'
          

            

              

    
    
    return render(request,template_name,{'signup_form':SignUpform})
