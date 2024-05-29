
from django.shortcuts import render
from django.views import View
from . models import Pproduct
from  django.db.models import Count

# Create your views here.
def home(request):
    return render(request,"home.html")
class CategoryView(View):
    def get(self,request,val):
        products=Pproduct.objects.filter(category=val)
        title=Pproduct.objects.filter(category=val).values('title')
        return render(request,"category.html",locals())
 
 