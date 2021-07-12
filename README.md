# Buddy
 This is an django project used to connect your assistant(buddy) for shopping. Simply as shopping buddy which helps in need during this pandemic. If you are not going out connect your buddy and they will come and bring all your essentials you needed.

# Prerequisites
 asgiref==3.3.4
 Django==3.2.4
 Pillow==8.2.0
 pkg-resources==0.0.0
 pytz==2021.1
 sqlparse==0.4.1
 
# Description
 In this project I have used Multiple Signup User
  - Assistant Signup
    -   class AssistantSignUp(UserCreationForm):<br />
              email = forms.CharField(max_length=20)<br />
              phone = forms.CharField(max_length=20)<br />

              pickup_location=forms.CharField(max_length=256)
              pincode=forms.CharField(max_length=20)


            class Meta(UserCreationForm.Meta):
                model= User
    
       

            @transaction.atomic
            def save(self):
                user=super().save(commit=False)
                user.email=self.cleaned_data.get('email')
                user.phone=self.cleaned_data.get('phone')
                user.pickup_location=self.cleaned_data.get('pickup_location')
                user.pincode=self.cleaned_data.get('pincode')
                user.is_assistant=True
                user.save()


                assistant=Assistant.objects.create(user=user)
                assistant.email=self.cleaned_data.get('email')
                assistant.phone=self.cleaned_data.get('phone')
                assistant.pickup_location=self.cleaned_data.get('pickup_location')
                assistant.pincode=self.cleaned_data.get('pincode')
        
                assistant.save()
                return user
      
  - Caller Signup
    -   class CallerSignUp(UserCreationForm):<br />
            email = forms.CharField(max_length=20)<br />
            phone = forms.CharField(max_length=20)<br />

            class Meta(UserCreationForm.Meta):
                model=User
        

            @transaction.atomic
            def save(self):
                user=super().save(commit=False)
                user.email=self.cleaned_data.get('email')
                user.phone=self.cleaned_data.get('phone')
             
                user.is_caller=True
                user.save()
      
                caller=Caller.objects.create(user=user)
                caller.email=self.cleaned_data.get('email')
                caller.phone=self.cleaned_data.get('phone')
       
                caller.save()
  
                return user

      



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

More optimization needed...
# Built With
 - Django - Web Framework
    

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
