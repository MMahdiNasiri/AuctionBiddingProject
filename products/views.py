from django.shortcuts import render
from django.views.generic import ListView
from .models import Products


class ProductsListView(ListView):
    queryset = Products.objects.filter(deleted=0)
    context_object_name = "products"

