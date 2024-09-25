from django.shortcuts import render
from rest_framework.throttling import UserRateThrottle ,AnonRateThrottle
from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class StudentThrottle(viewsets.ModelViewSet):
  queryset=Student.objects.all()
  print('Values of queryset is:',queryset)
  serializer_class=StudentSerializer
  authentication_classes= [SessionAuthentication]
  permission_classes = [IsAuthenticatedOrReadOnly]
  throttle_classes=[AnonRateThrottle,UserRateThrottle]
