from django.shortcuts import render
from .forms import *
from .models import*
# Create your views here.
def home(request):
    # form=Ragistration()
    form=RegistrationForm()
    # return render(request,"home.html",{"form":form})
    if request.method=="POST":
        # form=Ragistration(request.POST)
        form=RegistrationForm(request.POST)
        
        if form.is_valid():
            fname=form.cleaned_data["fname"]
            lname=form.cleaned_data["lname"]
            email=form.cleaned_data["email"]
            contact=form.cleaned_data["contact"]
            print(fname,lname,email,contact)
            user = Registration.objects.filter(email=email)
            if user:
                msg = "Email already exit"
                form = RegistrationForm()
                return render(request,"home.html",{"form":form,"msg":msg})
            else:
                form.save()
                msg="Registration succesfull"
                form=RegistrationForm()
                return render(request,"home.html",{"form":form,"msg":msg})
        
    #         # data={"fname":fname,"lname":lname,"email":email,"contact":contact}
    #         # RegistrationForm.object.create()
    #         form.save()
def login(request):
    form=LoginForm()
    return render(request,'login.html',{'form':form})