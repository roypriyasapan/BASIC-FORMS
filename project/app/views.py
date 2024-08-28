# from django.shortcuts import render
# from .forms import *
# from .models import*
# # Create your views here.
# def home(request):
#     # form=Ragistration()
#     form=RegistrationForm()
#     # return render(request,"home.html",{"form":form})
#     if request.method=="POST":
#         # form=Ragistration(request.POST)
#         form=RegistrationForm(request.POST)
        
#         if form.is_valid():
#             fname=form.cleaned_data["fname"]
#             lname=form.cleaned_data["lname"]
#             email=form.cleaned_data["email"]
#             contact=form.cleaned_data["contact"]
#             print(fname,lname,email,contact)
#             user = Registration.objects.filter(email=email)
#             if user:
#                 msg = "Email already exit"
#                 form = RegistrationForm()
#                 return render(request,"home.html",{"form":form,"msg":msg})
#             else:
#                 form.save()
#                 msg="Registration succesfull"
#                 form=RegistrationForm()
#                 return render(request,"home.html",{"form":form,"msg":msg})
        
#     #         # data={"fname":fname,"lname":lname,"email":email,"contact":contact}
#     #         # RegistrationForm.object.create()
#     #         form.save()
# def Login(request):
#     form=LoginForm()
#     if request.method== 'POST':
#             data=LoginForm(request.POST)
#             Login_email=form.cleaned_data["email"]
#             Login_contact=form.cleaned_data["contact"]
#             # print(email ,contact)
#             uder= Registration.objects.filter(email=Login_email)
#             if user:
#                  user = Registration.objects.get(email=Login_email)
#                  print(user)      

#     return render(request,'login.html',{'form':form})


# def login_data(request):
#     form=LoginForm()
#     if request.method== 'POST':
#             data=LoginForm(request.POST)
#             Login_email=form.cleaned_data["email"]
#             Login_contact=form.cleaned_data["contact"]
#             # print(email ,contact)
#             uder= Registration.objects.filter(email=Login_email)
#             if user:
#                  user = Registration.objects.get(email=Login_email)
#                  print(user)

from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

def home(request):
    form = RegistrationForm()
    if request.method=='POST':
        data = RegistrationForm(request.POST)
        if data.is_valid():
            name=data.cleaned_data['stu_name']
            email=data.cleaned_data['stu_email']
            city=data.cleaned_data['stu_city']
            contact=data.cleaned_data['stu_mobile']
            password = data.cleaned_data['stu_password']
            print(name,email,city,contact,password)
            data.save()
            msg="Registration Successfully"
            return render(request,'home.html',{'form':form,'msg':msg})
    else:
        return render(request,'home.html',{'form':form})
    
def login(request):
    form = LoginForm()
    if request.method=="POST":
        data = LoginForm(request.POST)
        if data.is_valid():
            email = data.cleaned_data['stu_email']
            password = data.cleaned_data['stu_password']
            # print(email,password)
            user = StudentModel.objects.filter(stu_email=email)
            
            if user:
                user = StudentModel.objects.get(stu_email=email)
                # print(user.stu_password)
                if user.stu_password==password:
                    name = user.stu_name
                    email = user.stu_email
                    contact = user.stu_mobile
                    city = user.stu_city
                    password = user.stu_password
                    data = {
                        'name':name,
                        'email':email,
                        'contact':contact,
                        'city':city,
                        'password':password
                    }
                    initial_data = {
                        'stu_name' : name,
                        'stu_email' : email
                    }
                    form1= QueryForm(initial=initial_data,)
                    return render(request,'dashboard.html',{'data':data,'query':form1})
                else:
                    msg = "Email & Password not matched"
                    return render(request,'login.html',{'form':form,'msg':msg})
            else:
                msg = "Email not register so please register first"
                return render(request,'login.html',{'form':form,'msg':msg})
    else:
        return render(request,'login.html',{'form':form})
    
def query(request):
        form = QueryForm()
        if request.method=="POST":
            query_data = QueryForm(request.POST)
            if query_data.is_valid():
                name = query_data.cleaned_data['stu_name']
                email = query_data.cleaned_data['stu_email']
                query = query_data.cleaned_data['stu_query']
                # print(email,name,query)
                query_data.save()
        if user:
            user = StudentModel.objects.get(stu_email=email)
            # print(user.stu_password)
            if user.stu_password==password:
                name = user.stu_name
                email = user.stu_email
                contact = user.stu_mobile
                city = user.stu_city
                password = user.stu_password
                data = {
                    'name':name,
                    'email':email,
                    'contact':contact,
                    'city':city,
                    'password':password
                }
                initial_data = {
                    'stu_name' : name,
                    'stu_email' : email
                }
                form1= QueryForm(initial=initial_data,)
                return render(request,'dashboard.html',{'data':data,'query':form1})