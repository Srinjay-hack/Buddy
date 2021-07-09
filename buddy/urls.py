
from django.contrib import admin
from django.urls import path,include
from accounts import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('caller/home/',include('caller.urls')),
    path('assistant/home/',include('assistant.urls')),
    

    
]
