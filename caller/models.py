from django.db import models
from django.urls.resolvers import LocalePrefixPattern
from accounts.models import Assistant,Caller

class Measurements(models.Model):
    location=models.CharField(max_length=256)
    destination=models.CharField(max_length=256)
    distance=models.DecimalField(max_digits=10,decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Distance from caller to assistance is {self.distance}"





class Connect(Assistant):
    is_connected=models.BooleanField(default=False)
