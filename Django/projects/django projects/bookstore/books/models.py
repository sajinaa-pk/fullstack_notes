from turtle import title
from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=50,null=False,blank=False)
    price=models.DecimalField(max_digits=4,decimal_places=2)
    author=models.CharField(max_length=100,null=False,blank=False)
    pages=models.IntegerField()
    class Meta:
        db_table='books'
