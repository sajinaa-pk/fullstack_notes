from django.shortcuts import render,redirect
from user.forms import userRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        x=userRegisterForm(request.POST)
        if x.is_valid():
            x.save()
            messages.success(request,'your account created successfully')
    x=userRegisterForm()
    return render(request,'register.html',{'form':x}) 

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            form=login(request,user)
            messages.success(request,'welcome')
            return redirect('home')
        else:
            messages.info(request,'user does not exist')    
    f=AuthenticationForm()
    return render(request,'login.html',{'form':f})    
    
       
