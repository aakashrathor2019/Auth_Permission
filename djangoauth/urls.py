"""
URL configuration for djangoauth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework.routers import DefaultRouter
from jwt_authn import views
from django.contrib import admin
from django.urls import path ,include


# router = DefaultRouter()
# router.register(r'studentapi', views.StudentModelView)
# router.register(r'studentapi', views.StudentList.as_view() , basename='student')

urlpatterns = [
    path('admin/',admin.site.urls),
    path('studentapi/', views.StudentList.as_view(), name='student-list'),
    path('auth/',include('rest_framework.urls' , namespace='rest_framework')),
]

