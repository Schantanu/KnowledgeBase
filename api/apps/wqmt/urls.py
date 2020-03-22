# appcards/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WQMTViewSet

router = DefaultRouter()
router.register(r'wqmt', WQMTViewSet)

urlpatterns = [
    path("", include(router.urls))
]