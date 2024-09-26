from django.shortcuts import render
from .serializers import PersonSerializer
from .models import Person
from rest_framework.generics import ListAPIView
from .mypagination import MyPageNumberPagination ,MyLimitOffSetPagination ,MyCursorPagination

class GlobalPagination(ListAPIView):
   queryset=Person.objects.all()
   serializer_class= PersonSerializer


class PageNumPagination(ListAPIView):
   queryset=Person.objects.all()
   serializer_class= PersonSerializer
   pagination_class= MyPageNumberPagination

class LimitOffSetpagination(ListAPIView):
   queryset=Person.objects.all()
   serializer_class=PersonSerializer
   pagination_class= MyLimitOffSetPagination

class CursorPaginationView(ListAPIView):
   queryset=Person.objects.all()
   serializer_class=PersonSerializer
   pagination_class=MyCursorPagination