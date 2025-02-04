"""
URL configuration for proje101 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from EventApp import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from EventApp.views import EventViewSet, RegistrationViewSet
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'registrations', RegistrationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('api/', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)