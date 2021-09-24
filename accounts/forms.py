from django import forms
from  django.contrib.auth.forms import UserCreationForm,UserChangeForm

from django.db import transaction

from .models import User,Assistant,Caller

#Assistant Signup Form
class AssistantSignUp(UserCreationForm):
    email = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)
    pickup_location=forms.CharField(max_length=256)
    pincode=forms.CharField(max_length=20)


    class Meta(UserCreationForm.Meta):
        model= User
    
       

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.phone=self.cleaned_data.get('phone')
        user.pickup_location=self.cleaned_data.get('pickup_location')
        user.pincode=self.cleaned_data.get('pincode')
        user.is_assistant=True
        user.save()


        assistant=Assistant.objects.create(user=user)
        assistant.email=self.cleaned_data.get('email')
        assistant.phone=self.cleaned_data.get('phone')
        assistant.pickup_location=self.cleaned_data.get('pickup_location')
        assistant.pincode=self.cleaned_data.get('pincode')
        
        assistant.save()
        return user



#Caller Signup Form

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




#Caller Edit Form
class CallerEdit(UserCreationForm):
    email = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)

    class Meta(UserCreationForm.Meta):
        model=User
        fields=['email','phone']
        

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



class AssistantEdit(UserChangeForm):
    email = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)
    is_available=forms.BooleanField()

    class Meta(UserChangeForm.Meta):
        model=Assistant
        fields=['email','phone','is_available']
        

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.phone=self.cleaned_data.get('phone')
        user.is_available=self.cleaned_data.get('is_available')
        user.is_assistant=True
        user.save()

        assistant=Assistant.objects.create(user=user)
        assistant.email=self.cleaned_data.get('email')
        assistant.phone=self.cleaned_data.get('phone')
        assistant.is_available=self.cleaned_data.get('is_available')
        assistant.save()
        return user


class CallerEdit(forms.ModelForm):
    
    class Meta:
        model=User
        fields={
            'username',
            'email',
            'phone',
        }

class AssistantEdit(forms.ModelForm):
    
    class Meta:
        model=User
        fields={
           
            'email',
            'phone',
            'is_available'
        }
      


#AddON Edit Form
class AddOn(forms.ModelForm):
    
    class Meta:
        model=Caller
        fields={
            
            'pickup_location',
            'pincode',
            'estimated_amount',
            'list_file',

        }



        