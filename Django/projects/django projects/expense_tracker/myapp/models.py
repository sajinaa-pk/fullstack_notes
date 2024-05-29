from django.db import models

# Create your models here.
class expense(models.Model):  
   
    exp    = models.CharField(max_length=100)  
    amt = models.IntegerField()  
    class Meta:  
        db_table = "expense"
        
class balance(models.Model):  
   
    bal    = models.IntegerField()  
    class Meta:  
        db_table = "balance"        
