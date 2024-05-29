
from django.db import models

# Create your models here.
class employee(models.Model):
	name=models.CharField(max_length=20)
	address=models.CharField(max_length=20)
	def __str__(self):
		return self.name

'''
python manage.py makemigrations
python manage.py migrate

IntegerField()          
BigIntegerField()
EmailField()
DateField()
DateTimeField()
TextField()
ImageField()

#from phonenumber_field.modelfields import PhoneNumberField
'''
	#Phonenumber=PhoneNumberField(blank=True)
'''	
	
		
The __str__ method just tells Django what to print 
 when it needs to print out an instance of the any model
'''












'''
class Meta:
	db_table = 'dbdemo_employee'
To generate a unique random nbr in model class
import random
def create_new_ref_number():
      return str(random.randint(1000, 9999))
	uid=models.CharField(
           max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number())

	#age=models.IntegerField()
'''
	


