from django.shortcuts import render, get_object_or_404

from .models import Category, Product

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)



def all_products(request):
    products = Product.objects.all()
    return render(request, "store/home.html", {"products": products})

