from rest_framework.pagination import PageNumberPagination ,LimitOffsetPagination,CursorPagination

#PageNumberClass
class MyPageNumberPagination(PageNumberPagination):
  page_size=2
  #page_query_param='q' {use for define alias of search variable in browser search bar}
  max_page_size=5


#LimitOffSetPagination Class
class MyLimitOffSetPagination(LimitOffsetPagination):
   default_limit=5

#Cursor Pagination Class
class MyCursorPagination(CursorPagination):
   page_size=2
   ordering='name'