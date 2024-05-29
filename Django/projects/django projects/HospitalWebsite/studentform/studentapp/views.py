from django.shortcuts import render,redirect
from .forms import studentForm
from .models import student

# Create your views here.
def index(request):
    if request.method=='POST':
        x=studentForm(request.POST)
        if x.is_valid():
            try:
                x.save()
                return redirect('/show')
            except:
                pass    
    x=studentForm()
    return render(request,'index.html',{'f':x})

def show(request):
    st=student.objects.all()
    return render(request,'show.html',{'students':st})  

def edit(request,pk):
    st=student.objects.get(id=pk)
    return render(request,'edit.html',{'student':st})

def update(request,x):
    st=student.objects.get(id=x)
    form=studentForm(request.POST,instance=st) 
    if form.is_valid():
        form.save()
        return redirect('/show') 
    return render(request,'edit.html',{'student':st})

def remove(request,pk):
    st=student.objects.get(id=pk)
    st.delete()
    return redirect('/show')    