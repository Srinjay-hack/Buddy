from django.urls import path
from . views import *
urlpatterns=[
    path('',main,name="Signup"),
    path('accounts/signup/caller',CallerSignUpView.as_view(),name="caller_signup"),
    path('accounts/signup/assistant',AssistantSignUpView.as_view(),name="assistant_signup"),
    path('accounts/sigin/caller',CallerloginUser,name="caller_signin"),
    path('accounts/sigin/assistant',AssistantloginUser,name="assistant_signin"),
    path('accounts/caller/home',Callerhome,name="caller_home"),
    path('accounts/assistant/home',Assistanthome,name="assistant_home"),
    path('accounts/edit/caller',CallerEditView.as_view(),name="edit_profile_caller"),
    path('accounts/edit/caller',AssistantEditView.as_view(),name="edit_profile_assistant"),
    



]