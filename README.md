# Buddy
 This is an django project used to connect your assistant(buddy) for shopping. Simply as shopping buddy which helps in need during this pandemic. If you are not going out connect your buddy and they will come and bring all your essentials you needed.

# Optimization Code

### views.py
 def addOn(request):
    try:
        profile = request.user.caller
    except Caller.DoesNotExist:
        profile = Caller(user=request.user)
    


        
    if request.method=='POST':
        form=AddOn(request.POST,instance=profile)

        pincode = request.POST.get('pincode')

        
         
        if form.is_valid():
            all_assistant=list(Assistant.objects.filter(pincode=pincode))
            count=Assistant.objects.filter(pincode=pincode).count()
            all_assistant=random.sample(all_assistant,count)[0]
            
            form.save()
            return render (request,"caller/connect1.html",{'Assistants': all_assistant})
            

    else:
        form=AddOn(instance=profile)
        args={'form':form}
        return render(request,"caller/addOn.html",args) 


### forms.py
 class AddOn(forms.ModelForm):
    
    class Meta:
        model=Caller
        fields={
            'pickup_location',
            'pincode',

        }

  

# License

 Copyright 2021 Srinjay Mondal

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
