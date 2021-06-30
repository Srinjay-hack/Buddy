from django import forms
from  django.contrib.auth.forms import UserCreationForm

from django.db import transaction

from .models import User,Assistant,Caller


class AssistantSignUp(UserCreationForm):
    email = forms.EmailField(required=True)
    phone=forms.CharField(max_length=20)


    class Meta(UserCreationForm.Meta):
        model=User

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_assistant=True
        user.save()
        assistant=Assistant.objects.create(user=user)
        assistant.phone=self.cleaned_data.get('phone')
        assistant.save()
        return user



class CallerSignUp(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model=User

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_caller=True
        user.save()
        caller=Caller.objects.create(user=user)
        return user


