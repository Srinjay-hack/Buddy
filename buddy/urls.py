
from django.contrib import admin
from django.urls import path,include
from accounts import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('caller/home/',include('caller.urls')),
    path('assistant/home/',include('assistant.urls')),    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)