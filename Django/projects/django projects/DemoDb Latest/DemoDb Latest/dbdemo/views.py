from django.shortcuts import render
from .models import employee

def index(request):
	return render(request,"index.html")
def addemployee(request):
	responseDic={}
	try:
		Name=request.POST['name']   
		Address=request.POST['address'] 
		emplist=employee(name=Name,address=Address)
#or emplist=employee.objects.create(name=Name,address=Address)
		emplist.save()
		responseDic["msg"]="Employee added"
		return render(request,"index.html",responseDic)
	except Exception as e:
		print(e) 	
		responseDic["msg"]="Employee cannot be added"
		return render(request,"index.html",responseDic)


def display(request):
	empdtls=employee.objects.all()
	return render(request,"index.html",{'emp':empdtls})



#Delete by passing id to url

def delete(request,eid):
	empdtls=employee.objects.get(id=eid)
	empdtls.delete()
	return render(request,"index.html",{'msg':"Deleted"})

#Delete using name

def delemployee(request):
	Name=request.POST['name'] 
	empdtls=employee.objects.filter(name=Name)
	empdtls.delete()
	return render(request,"index.html",{'msg':"Deleted"})


def updatename(request):
	#Update using get()
	oldname=request.POST["oldname"]
	newname=request.POST["newname"]
	emp=employee.objects.get(name=oldname)
	emp.name=newname
	emp.save()
	return render(request,"index.html",{'msg':"Updated"})

	#Update using filter
	try:
		oldname=request.POST["oldname"]
		newname=request.POST["newname"]
		emp=employee.objects.filter(name=oldname)
		if emp.exists():
			emp.update(name=newname)
			return render(request,"index.html",{'msg1':"Updated"})
		else:
			return render(request,"index.html",{'msg1':"No records found"})
	except Exception as e:
		print(e)
		return render(request,"index.html",{'msg1':"Not Updated"})










		
	



	


