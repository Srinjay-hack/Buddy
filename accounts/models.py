from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_assistant=models.BooleanField(default=False)
    is_caller=models.BooleanField(default=False)


class Assistant(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone=models.CharField(max_length=20)
    pickup_location=models.CharField(max_length=256)
    




    def __str__(self) :
        return self.user.username

    

class Caller(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone=models.CharField(max_length=20)
    pickup_location=models.CharField(max_length=256)


    def __str__(self) :
        return self.user.username
   