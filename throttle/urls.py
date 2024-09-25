from django.urls import path
from .views import StudentThrottle

urlpatterns = [
    path('student1/', StudentThrottle.as_view({'get': 'list', 'post': 'create'}), name='student1'),
]
