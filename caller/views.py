from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

def landing(response):
    return render(response, 'landingpage/landing.html')


def signin(response):
    return render(response,"caller/signin.html")    

def register(response):
    if(response.method=='POST'):
        username=response.POST.get("username", "default value")
        email=response.POST.get("email", "default value")
        #number=response.POST.get("contact_info", "default value")
        password1=response.POST.get("password", "default value")
        password2=response.POST.get("password", "default value")


        user=User.objects.create_user(username=username,password=password1,email=email) 
        user.save()


    else:
        return render(response,"caller/register.html")   