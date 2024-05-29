from django.urls import path
from .import views

urlpatterns = [
    path('',views.index), 
   	path('add',views.addemployee),
    path('del',views.delemployee),
    path('display',views.display),
    path('delete/<int:eid>',views.delete),
    path('update',views.updatename)

]