from django import forms
from  django.contrib.auth.forms import UserCreationForm

from django.db import transaction

from .models import User,Assistant,Caller


class AssistantSignUp(UserCreationForm):
    email = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)


    class Meta(UserCreationForm.Meta):
        model= User
       

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.phone=self.cleaned_data.get('phone')
        user.is_assistant=True
        user.save()


        assistant=Assistant.objects.create(user=user)
        assistant.email=self.cleaned_data.get('email')
        assistant.phone=self.cleaned_data.get('phone')
        assistant.save()
        return user



class CallerSignUp(UserCreationForm):
    email = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)

    class Meta(UserCreationForm.Meta):
        model=User
        

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.phone=self.cleaned_data.get('phone')
        user.is_caller=True
        user.save()

        caller=Caller.objects.create(user=user)
        caller.email=self.cleaned_data.get('email')
        caller.phone=self.cleaned_data.get('phone')
        caller.save()
        return user



class AddOn(UserCreationForm):
    pickup_location=forms.CharField(max_length=256)
    pincode=forms.CharField(max_length=20) 

    class Meta:
        model=User

    @transaction.atomic 
    def save(self):
        pass   





