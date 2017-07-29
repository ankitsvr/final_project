# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime
from app1.forms import SignUpform
from app1.forms import loginform
from app1.models import Usermodel1
from django.contrib.auth.hashers import make_password,check_password
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
         if signup_form.is_valid():

              #data is valid succefully

              username=signup_form.cleaned_data['username']
              name=signup_form.cleaned_data['name']
              email=signup_form.cleaned_data['email']
              password=signup_form.cleaned_data['password']
              user = Usermodel1(name=name, password=make_password(password), email=email, username=username)
              user.save()
              template_name='login.html'
          

    return render(request,template_name,{'signup_form':SignUpform})

def login_view(request):
    if request.method =='GET':

        #display login form
        login_form=loginform()
        template_name='login.html'

    elif request.method =='POST':
        login_form= loginform(request.POST)
        if login_form.is_valid():
            #validation
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            #read data from data base
            user=Usermodel1.objects.filter(username=username).first()
            if user:
                #cmpare pass.
                if check_password(password,user.password):
                    #login succefully

                    template_name='login_success.html'


                else:
                    #does not login
                     template_name='login_fail.html'
            else:
                #user ds not exist in db
                template_name='login_fail.html'

        else:        
             
            print"validation failed"
            template_name='login_fail.html'



    return render(request, template_name, {'login_form':login_form })





            
