
from django.contrib import admin
from django.urls import path,include
from caller import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('assistant.urls',)),
    path('', include('accounts.urls')), 
    #path('caller/', include('caller.urls')),
    #path('accounts/', include('accounts.urls')),
]
