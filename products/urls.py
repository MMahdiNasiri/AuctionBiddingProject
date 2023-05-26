from django.urls import path, include

from .views import ProductsListView, SellerProductsListView, ProductDetailView

urlpatterns = [
    path('products/', ProductsListView.as_view()),
    path("products/<seller>/user/", SellerProductsListView.as_view()),
    path("products/<slug:slug>/detail/", ProductDetailView.as_view(), name="product-detail"),
    path('api/', include('products.api.urls')),
]
