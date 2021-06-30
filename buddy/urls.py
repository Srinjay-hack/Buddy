
from django.contrib import admin
from django.urls import path,include
from accounts import views




urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('assistant.urls',)),
    #path('', include('caller.urls')),
    path('',include('accounts.urls')),

    
]
