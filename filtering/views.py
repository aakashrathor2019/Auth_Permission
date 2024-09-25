from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView 
from .models import Employee
from .serializers import EmployeeSerializer
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


# Filter Data using filter method
class NormalFilter(ListAPIView):
  queryset=Employee.objects.all()
  serializer_class=EmployeeSerializer
  authentication_classes=[SessionAuthentication]
  permission_classes=[IsAuthenticatedOrReadOnly]
  
  def get_queryset(self):
    user=self.request.user
    return Employee.objects.filter(
      Q(name__istartswith='a') | Q(pos__iexact='Software Developer')
    )
  

#Filter data using filterset_fields 
class FilterSetFilter(ListAPIView):
  queryset=Employee.objects.all()
  serializer_class=EmployeeSerializer
  authentication_classes=[SessionAuthentication]
  permission_classes=[IsAuthenticatedOrReadOnly]
  filterset_fields=['pos']


#Filter Data Using filterbackends 
class FilterBackendsFilter(ListAPIView):
  queryset=Employee.objects.all()
  serializer_class=EmployeeSerializer
  authentication_classes=[SessionAuthentication]
  permission_classes=[IsAuthenticatedOrReadOnly]
  filter_backends=[DjangoFilterBackend]
  filterset_fields=['name']


#Filter data using search filter class
class SearchFilter(ListAPIView):
  queryset=Employee.objects.all()
  serializer_class=EmployeeSerializer
  authentication_classes=[SessionAuthentication]
  permission_classes=[IsAuthenticatedOrReadOnly]
  filter_backends=[SearchFilter]
  search_fields=['name','pos']
  
