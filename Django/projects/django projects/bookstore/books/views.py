from django.shortcuts import render
from .serializers import bookserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import book
from django.http import HttpResponse

# Create your views here.
@api_view(['POST'])
def Createbook(request):
    s=bookserializer(data=request.data)
    if s.is_valid():
        s.save()
    return Response(s.data) 

@api_view(['GET'])
def showall(request):
    Books=book.objects.all()
    s=bookserializer(Books,many=True)
    return Response(s.data)

@api_view(['GET'])
def viewBook(request,pk):
    Books=book.objects.get(id=pk)
    s=bookserializer(Books,many=False)
    return Response(s.data)    

@api_view(['POST'])
def updateBook(request,pk):
    Books=book.objects.get(id=pk)
    s=bookserializer(instance=Books,data=request.data)
    if s.is_valid():
        s.save()
    return Response(s.data)    

@api_view(['GET'])
def removebook(request,pk):
    Books=book.objects.get(id=pk)
    Books.delete()
    return Response('deleted') 


def index(request):
    request.session['name']='abcd'
    request.session['email']='abc@gmail.com'
    return HttpResponse('sesion set') 

def getsession(request):
    x=request.session['name'] 
    return HttpResponse(x)  

def setcookie(request):
    x=HttpResponse('cookie set')
    x.set_cookie('name','abcd')
    return x 

def getcookie(request):
 x=request.COOKIES['name'] 
 return HttpResponse(x)


