from django.urls import path
from . views import *
urlpatterns=[
    path('',main,name="Signup"),
    path('signup/caller',CallerSignUpView.as_view(),name="caller_signup"),
    path('signup/assistant',AssistantSignUpView.as_view(),name="assistant_signup"),
    path('sigin/caller',CallerloginUser,name="caller_signin"),
    path('sigin/assistant',AssistantloginUser,name="assistant_signin"),
    path('caller/home',Callerhome,name="caller_home"),
    path('assistant/home',Assistanthome,name="assistant_home"),
    path('edit/caller',CallerEditView.as_view(),name="edit_profile_caller"),
    path('edit/caller/',AssistantEditView.as_view(),name="edit_profile_assistant"),
    path('connect/caller/',addOn,name="caller_addOn"),
    



]