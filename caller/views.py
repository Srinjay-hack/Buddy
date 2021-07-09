from django.shortcuts import render,redirect
from accounts.models import  Caller

# Create your views here.
from .forms import Createfile


def main(request):
    return render(request,"caller/connect.html",{})



def choosefile(request):
    try:
        profile = request.user.caller
    except Caller.DoesNotExist:
        profile = Caller(user=request.user)

    if request.method=='POST':
        form=Createfile(request.POST,instance=profile)
         
        if form.is_valid():
            form.save()
            return redirect('file_caller')

    else:
        form=Createfile(instance=profile)
        args={'form':form}
        return render(request,"caller/connect.html",args) 