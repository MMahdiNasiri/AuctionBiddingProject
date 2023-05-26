from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CategoryViewSet, PictureViewSet

router = DefaultRouter()

router.register('product', ProductViewSet)
router.register('category', CategoryViewSet)
router.register('picture', PictureViewSet)


urlpatterns = [
    path('', include(router.urls))
]
