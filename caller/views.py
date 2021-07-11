from django.shortcuts import render,redirect,get_object_or_404
from accounts.models import  Caller ,Assistant

# Create your views here.
from .forms import Createfile
from .models import Measurements

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



def calulate_distance_view(request):

   
    return render(request,"caller/connect.html",{})


'''
def show_assistant(request):
    all_assiatant=request.Assistant.objects.all()
    return render (request, "caller/connecct1.html", all_assiatant)
'''
