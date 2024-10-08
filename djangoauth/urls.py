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
from django.urls import path, include

router = DefaultRouter()
router.register(r'student', views.StudentModelView, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Use router for jwt_authn app
    path('throttle/',include('throttle.urls')),
    path('filter/',include('filtering.urls')),
    path('pagination/',include('pagination.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]

