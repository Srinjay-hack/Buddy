from django.contrib import admin

# Register your models here.
from accounts.models import User,Assistant,Caller

admin.site.register(User)

admin.site.register(Assistant)

admin.site.register(Caller) 