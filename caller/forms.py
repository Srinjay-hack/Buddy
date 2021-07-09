from django import forms
from  django.contrib.auth.forms import UserCreationForm,UserChangeForm

from django.db import transaction

from accounts.models import Caller
from .models import Measurements



class Createfile(forms.ModelForm):
    class Meta:
        model=Caller
        
        fields={
            'estimated_amount',
            'list_file',
        }



class MeasurementModelForm(forms.ModelForm):
    class Meta:
        model=Measurements
        fields=('destination',)