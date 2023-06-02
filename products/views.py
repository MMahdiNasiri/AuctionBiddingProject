from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from rest_framework import filters, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet
# from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ProductSerializer, CategorySerializer, ProductPictureSerializer
from .models import Products, Category, ProductPictures


class ProductViewSet(ModelViewSet):
    # it's better to change owner or read only
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Products.objects.filter(deleted=0)
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    # search_fields = ["content"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(deleted=0)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PictureViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductPictureSerializer
    queryset = ProductPictures.objects.all()


class ProductsListView(ListView):
    queryset = Products.objects.filter(deleted=0)
    context_object_name = "products"


class ProductDetailView(DetailView):
    queryset = Products.objects.filter(deleted=0)
    context_object_name = "product"
    slug_field = 'identifier'


# we must change it to get from the auth not url
class SellerProductsListView(ListView):
    template_name = "products_list.html"
    context_object_name = "products"

    def get_queryset(self):
        seller = get_object_or_404(User, username=self.kwargs["seller"])
        return Products.objects.filter(seller=seller)
