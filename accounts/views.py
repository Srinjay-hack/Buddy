from django.shortcuts import render,redirect
from  django.contrib.auth import login

# Create your views here.
from django.views.generic import CreateView
from .forms import AssistantSignUp,CallerSignUp
from .models import User,Assistant,Caller

def main(request):
    return render(request,"landingpage/landing.html",{})



class CallerSignUpView(CreateView):
    model=User
    form_class = CallerSignUp
    template_name="caller/register.html"

    def get_context_data(self,**kwargs):
        kwargs['user_type'] = 'caller'
        return super().get_context_data (**kwargs)


    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return redirect('Signup')

class AssistantSignUpView(CreateView):
    model=User
    form_class = AssistantSignUp
    template_name="assistant/register.html"

    def get_context_data(self,**kwargs):
        kwargs['user_type'] = 'caller'
        return super().get_context_data (**kwargs)


    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return redirect('Signup')








    
