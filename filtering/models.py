from django.db import models

# Create your models here.
class Employee(models.Model):
  name=models.CharField(max_length=50)
  emp_id=models.IntegerField()
  pos=models.CharField(max_length=50)
  joining_date= models.DateTimeField()
