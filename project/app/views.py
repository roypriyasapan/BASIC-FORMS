from django.shortcuts import render
from .forms import RegistrationForm
from .models import Registration



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
            # data={"fname":fname,"lname":lname,"email":email,"contact":contact}
            # RegistrationForm.object.create()
            form.save()
    return render(request,"home.html",{"form":form})