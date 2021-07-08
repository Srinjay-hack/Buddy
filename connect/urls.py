from django.urls import path
from . views import *
urlpatterns=[
    path('connect',main,name="connect_caller")
  

]