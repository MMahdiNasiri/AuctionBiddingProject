from django.urls import path

from .views import ProductsListView, SellerProductsListView, ProductDetailView

urlpatterns = [
    path('products/', ProductsListView.as_view()),
    path("products/<seller>/user/", SellerProductsListView.as_view()),
    path("<slug:slug>/product/", ProductDetailView.as_view(), name="product-detail"),
]
