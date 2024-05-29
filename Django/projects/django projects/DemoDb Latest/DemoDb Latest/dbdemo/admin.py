from django.contrib import admin
from .models import employee


#admin.site.register(employee)


#To create admin
#python manage.py createsuperuser



class EmployeeAdmin(admin.ModelAdmin):
    #fields=('name','address') 
    list_display=('name','address')
    ordering = ('address',)
    search_fields = ('name','address')
admin.site.register(employee,EmployeeAdmin)


