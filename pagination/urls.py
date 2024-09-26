from django.urls import path
from . views import GlobalPagination ,PageNumPagination,LimitOffSetpagination,CursorPaginationView


urlpatterns=[
    path('globalpagination/', GlobalPagination.as_view(),name='globalpagination'),
    path('pagenumpagination/', PageNumPagination.as_view(),name='pagenumpagination'),
    path('limitoffsetpagination/', LimitOffSetpagination.as_view(),name='limitoffsetpagination'),
    path('cursorpagination/', CursorPaginationView.as_view(),name='cursorpagination'),
]