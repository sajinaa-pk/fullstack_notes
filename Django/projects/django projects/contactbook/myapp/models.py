from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    class Meta:
        db_table='contactbook'
        