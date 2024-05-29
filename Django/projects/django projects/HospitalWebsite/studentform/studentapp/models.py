from django.db import models

# Create your models here.
class student(models.Model):
    sid=models.CharField(max_length=50)
    sname=models.CharField(max_length=100)
    semail=models.EmailField()
    scontact=models.CharField(max_length=100)
    class Meta:
        db_table='student'