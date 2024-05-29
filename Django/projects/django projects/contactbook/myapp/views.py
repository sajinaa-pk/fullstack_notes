from django.shortcuts import render
from myapp.forms import phoneForm
from myapp.models import contact
from myapp.forms import nameform
from myapp.forms import phoneform

p=phoneForm()
response={}
response['form']=p
contacts=contact.objects.all()
response['contacts']=contacts
response['form1']=nameform()
response['form2']=phoneform()

# Create your views here.
def index(request):
  
    return render(request,'index.html',response)

def addcontact(request):
    try:
        n=request.POST['name']
        p=request.POST['phone']
        contacts=contact.objects.all()
        for i in contacts:
            if n in i.name:
                response['res']='contact name already exists'
                return render(request,'index.html',response)
        contacts=contact(name=n,phone=p) 
        contacts.save()
        response['contacts']=contact.objects.all()
        response['res']='contact added'  
        return render(request,'index.html',response) 
    except Exception as e:
        print(e)
        response['res']='contact can not be added'
        return render(request,'index.html',response)         
def updatename(request):
    try:
        oldname=request.POST['oname']
        newname=request.POST['nname']
        contacts=contact.objects.get(name=oldname)
        if oldname in contacts.name:
            contacts.name=newname
            contacts.save()
            response['res1']='contact name updated'
            response['contacts']=contact.objects.all()
            return render(request,'index.html',response)
        else:
            response['res1']='contact name cannot be updated'
            return render(request,'index.html',response)    
    except Exception as e:
        print(e)
        response['res1']='contact name cannot be updated'
        return render(request,'index.html',response)

def updatephone(request):
    try:
        n=request.POST['name']
        newno=request.POST['newnumber']
        contacts=contact.objects.get(name=n)
        if n in contacts.name:
            contacts.phone=newno
            contacts.save()
            response['res2']='phone number updated'
            response['contacts']=contact.objects.all()
            return render(request,'index.html',response)        
        else:
            response['res2']='phone number can not be updated'
            return render(request,'index.html',response)
    except Exception as e:
        print(e)   
        response['res2']='phone number can not be updated'
        return render(request,'index.html',response)     
