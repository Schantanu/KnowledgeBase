# appcards/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CRUDViewSet

router = DefaultRouter()
router.register(r'crud', CRUDViewSet)

urlpatterns = [path("", include(router.urls))]
