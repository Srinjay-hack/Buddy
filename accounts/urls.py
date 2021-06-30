from django.urls import path
from . views import *
urlpatterns=[
    path('',main,name="Signup"),
    path('accounts/signup/caller',CallerSignUpView.as_view(),name="caller_signup"),
    path('accounts/signup/assistant',AssistantSignUpView.as_view(),name="assistant_signup"),

]