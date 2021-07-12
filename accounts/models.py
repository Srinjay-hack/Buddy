from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    pickup_location=models.CharField(max_length=256)
    pincode=models.CharField(max_length=20)
    
    is_assistant=models.BooleanField(default=False)
    is_caller=models.BooleanField(default=False)


class Assistant(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    pickup_location=models.CharField(max_length=256)
    pincode=models.CharField(max_length=20)
    is_available=models.BooleanField(default=False)


    
    def __str__(self) :
        return self.user.username

    

class Caller(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    pickup_location=models.CharField(max_length=256)
    pincode=models.CharField(max_length=20)
    estimated_amount=models.IntegerField(default=0)
    list_file=models.FileField(upload_to ='uploads/')




    def __str__(self) :
        return self.user.username
   