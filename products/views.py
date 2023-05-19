from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Products


class ProductsListView(ListView):
    queryset = Products.objects.filter(deleted=0)
    context_object_name = "products"


class SellerProductsListView(ListView):
    template_name = "products_list.html"
    context_object_name = "products"

    def get_queryset(self):
        seller = get_object_or_404(User, username=self.kwargs["seller"])
        return Products.objects.filter(seller=seller)
