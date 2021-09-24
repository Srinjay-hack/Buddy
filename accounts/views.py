from django.shortcuts import render,redirect
from  django.contrib.auth import login
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.
from django.views.generic import CreateView
from .forms import AssistantSignUp,CallerSignUp,CallerEdit,AssistantEdit,AddOn
from .models import User,Assistant,Caller
import random

#landingpage
def main(request):
    return render(request,"landingpage/landing.html",{})


#callersignupview
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
        return redirect('caller_home')


#assistantsignupform
class AssistantSignUpView(CreateView):
    model=User
    form_class = AssistantSignUp
    template_name="assistant/register.html"

    def get_context_data(self,**kwargs):
        kwargs['user_type'] = 'assistant'
        return super().get_context_data (**kwargs)


    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return redirect('assistant_home')


#AssistantloginUser
def AssistantloginUser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password=request.POST.get('password')

        if username and password:

            user=authenticate(username=username,password=password)

            if user  is not None:
                login(request,user)
                return redirect('assistant_home')

            else:
                messages.error(request,"Username or Password is invalid")
        else:
            messages.error(request,'Fill out alll the fields')


    
    return render(request,'assistant/signin.html',{})  


#CallerloginUser
def CallerloginUser(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:

            caller=authenticate(username=username,password=password)

            if caller  is not None:
                login(request,caller)
                return redirect('caller_home')

            else:
                messages.error(request,"Username or Password is invalid")
        else:
            messages.error(request,'Fill out alll the fields')


    
    return render(request,'caller/signin.html',{})      





#logout
def logoutUser(request):
    logout(request)
    return redirect('Signup')



#callerhome
def Callerhome(request):
    return render(request,"caller/home.html",{}) 

#assistanthome
def Assistanthome(request):
    
    return render(request,"assistant/home.html",{}) 




#CallerEditView
class CallerEditView(generic.UpdateView):
    form_class=CallerEdit
    template_name="caller/edit_profile.html"
    success_url=reverse_lazy("caller_home")
    
    def get_object(self):
        return self.request.user    

#AssistantEditView
class AssistantEditView(generic.UpdateView):
    form_class=AssistantEdit
    template_name="assistant/edit_profile.html"
    success_url=reverse_lazy("assistant_home")
    
    def get_object(self):
        return self.request.user            

    

#addON Pincodes->and Address edit
def addOn(request):
    try:
        profile = request.user.caller
    except Caller.DoesNotExist:
        profile = Caller(user=request.user)
        
    if request.method == 'POST':
        form=AddOn(request.POST,request.FILES or None, instance=profile)

        pincode = request.POST.get('pincode')
         
        if form.is_valid():

            try:

                all_assistant=list(Assistant.objects.filter(pincode=pincode,is_available=True))
                count=Assistant.objects.filter(pincode=pincode,is_available=True).count()
                all_assistant=random.sample(all_assistant,count)[0]

            except IndexError as e:
                return render(request,"caller/feedback.html",{})  

            
            form.save()
            instance=form.save(commit=False)
            instance.save()
            context={

            'Assistants': all_assistant,
            'form':form,
            'instance':instance
            }

            return render (request,"caller/connect1.html",context)       

    else:
        form=AddOn(instance=profile)
        args={'form':form}
        return render(request,"caller/addOn.html",args) 

         
'''
def caller_connected(request):
        
    pincode = request.POST.get('pincode')

    all_assistant=Assistant.objects.filter(pincode=pincode)
    return render (request,"caller/connect1.html",{'Assistants': all_assistant})
'''




