# appcards/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppCardsViewSet

router = DefaultRouter()
router.register(r'appcards', AppCardsViewSet)

urlpatterns = [
    path("", include(router.urls))
]