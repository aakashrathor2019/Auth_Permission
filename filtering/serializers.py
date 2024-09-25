from .models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model=Employee
    fields=['id','name','emp_id','pos','joining_date']