from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('connect/',main,name="connect_caller"),
    path('connect/file',choosefile,name="file_caller"),
   
]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
