from django.urls import path
from . import views

urlpatterns=[
    path('', views.index,name="index"),
    path("register/",views.registerUser,name="register"),
    path("signin/",views.loginUser,name="signin"),
    path("home/",views.home,name="home"),
    path("logout/",views.logoutUser,name="logout"),



]