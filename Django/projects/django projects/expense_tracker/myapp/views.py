
from django.shortcuts import render,redirect

# Create your views here.
from myapp.forms import expform
from myapp.forms import balform
from .models import expense
from .models import balance
from django.contrib import messages 
from django.contrib.auth import authenticate, login,logout 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegisterForm

@login_required 
def expense_tracker(request):  
    x = expform()
    y= balform()
    try:
       summary = expense.objects.all()
       bal=balance.objects.get(id=1)
       bal=bal.bal
       return render(request,"index.html",{'form':x,'form1':y,'expense':summary,'bal':bal})
    except Exception as e:    
        print(e)
        summary = expense.objects.all()
        bal=0
        return render(request,"index.html",{'form':x,'form1':y,'expense':summary,'bal':bal})
@login_required  
def addbalance(request):
    x = expform()
    y= balform()
    try:
      
        currentbal=balance.objects.get(id=1)
        addamt=int(request.POST['bal'])
        newamount=currentbal.bal+addamt 
        currentbal.bal=newamount
        currentbal.save()
        res="balance updated successfully" 
        summary = expense.objects.all()
        bal=balance.objects.get(id=1)
        bal=bal.bal
        return render(request,"index.html",{'form':x,'form1':y,'res':res,'expense':summary,'bal':bal})
    except Exception as e:
        print(e)
        bal=balance.objects.get(id=1)
        res="bal not updated"
        summary = expense.objects.all()
        return render(request,"index.html",{'form':x,'form1':y,'res':res,'expense':summary,'bal':bal})

@login_required 
def addexpense(request):
    x = expform()
    y= balform()
    try:
        
        
        exp=request.POST['exp']
        amt=int(request.POST['amt'])
        bal=balance.objects.get(id=1)
        if(amt>bal.bal):
            res1="insufficient balance"
            
        else:
        
            newbal=bal.bal-amt 
            bal.bal=newbal
            bal.save()
            obj=expense(exp=exp,amt=amt)
            obj.save()
            res1="expense added successfully"            
            summary = expense.objects.all()
            bal=balance.objects.get(id=1)
            bal=bal.bal            
        return render(request,"index.html",{'form':x,'form1':y,'res1':res1,'expense':summary,'bal':bal})
    except Exception as e:
        print(e)
        res1="expense not updated"
        summary = expense.objects.all()
        bal=balance.objects.get(id=1)
        bal=bal.bal
        return render(request,"index.html",{'form':x,'form1':y,'res1':res1,'expense':summary,'bal':bal})


def index(request): 
    return render(request, 'ind.html', {'title':'index'})
def register(request): 
    
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            messages.success(request, f'Your account has been created ! You are now able to log in') 
            return redirect('login') 
    else: 
        form = UserRegisterForm() 
    return render(request, 'register.html', {'form': form, 'title':'reqister here'})
    
    
def Login(request): 
    if request.method == 'POST': 
   
        # AuthenticationForm_can_also_be_used__ 
   
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username = username, password = password) 
        if user is not None: 
            form = login(request, user) 
            messages.success(request, f' wecome {username} !!') 
            x = expform()
            y= balform()
            try:
               summary = expense.objects.all()
               bal=balance.objects.get(id=1)
               bal=bal.bal
               return render(request,"index.html",{'form':x,'form1':y,'expense':summary,'bal':bal})
            except Exception as e:    
                print(e)
                summary = expense.objects.all()
                bal=0
                return render(request,"index.html",{'form':x,'form1':y,'expense':summary,'bal':bal}) 
        else: 
            messages.info(request, f'account done not exit plz sign in') 
    form = AuthenticationForm() 
    return render(request, 'login.html', {'form':form, 'title':'log in'}) 


        
