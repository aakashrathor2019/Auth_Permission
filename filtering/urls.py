from django.urls import path
from . views import NormalFilter ,FilterSetFilter ,FilterBackendsFilter,SearchFilter,SybmolicSerach,OrderingFilter

urlpatterns=[
   path('normal/',NormalFilter.as_view(),name='normal'),
   path('filterset/',FilterSetFilter.as_view(),name='filterset'),
   path('filterbackend/',FilterBackendsFilter.as_view(),name='filterbackend'),
   path('searchfilter/',SearchFilter.as_view(),name='searchfilter'),
   path('symbolicsearch/',SybmolicSerach.as_view(),name='symbolicsearch'),
   path('orderingfilter/',OrderingFilter.as_view(),name='orderingfilter'),
]