from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Products


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
