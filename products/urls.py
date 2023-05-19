from django.urls import path

from .views import ProductsListView, SellerProductsListView

urlpatterns = [
    path('products/', ProductsListView.as_view()),
    path("products/<seller>/", SellerProductsListView.as_view()),
]
