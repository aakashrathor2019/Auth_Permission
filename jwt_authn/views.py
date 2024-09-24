from django.shortcuts import render
from .models import Student 
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication ,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions ,AllowAny,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.throttling import AnonRateThrottle , UserRateThrottle



class StudentModelView(viewsets.ModelViewSet):
  queryset= Student.objects.all()
  serializer_class= StudentSerializer
  #authentication_classes=[BasicAuthentication]
  #permission_classes=[IsAuthenticated]
  authentication_classes=[SessionAuthentication]
  permission_classes=[IsAuthenticatedOrReadOnly]
  throttle_classes= [AnonRateThrottle , UserRateThrottle]
  # permission_classes=[DjangoModelPermissions]
  # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]

