from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login , logout
from .forms import Registerform
from django.contrib import messages

def registerUser(request):
    form = Registerform()
    if request.method == "POST":
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')

    else:
        form=Registerform()

    return render(request,"assistant/register.html",{'form':form})


def loginUser(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password=request.POST.get('password')

        if username and password:

            user=authenticate(username=username,password=password)

            if user  is not None:
                login(request,user)
                return redirect('home')

            else:
                messages.error(request,"Username or Password is invalid")
        else:
            messages.error(request,'Fill out alll the fields')


    
    return render(request,'assistant/signin.html',{})    
    
def index(request):
    return render(request,"landingpage/landing.html",{})


def home(request):
    return render(request,"assistant/home.html",{}) 


def logoutUser(request):
    logout(request)
    return redirect('index')



