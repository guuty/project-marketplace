from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, "market/home.html")

def product_list(request):
    products = Product.objects.filter(active=True).order_by("-created_at")
    return render(request, "product_list.html", {"products": products})
