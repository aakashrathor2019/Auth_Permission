from django.db import models

# Create your models here.
class Person(models.Model):
   name=models.CharField(max_length=50)
   p_id=models.IntegerField()
   address=models.CharField(max_length=50)
   contact=models.CharField(max_length=10)