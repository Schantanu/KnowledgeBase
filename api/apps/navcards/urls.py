from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import RecipeViewSet
from .views import NavCardsViewSet

router = DefaultRouter()
# router.register(r'navcards', RecipeViewSet)
router.register(r'navcards', NavCardsViewSet)

urlpatterns = [path("", include(router.urls))]
