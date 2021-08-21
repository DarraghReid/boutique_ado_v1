from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """
    View to show all products, sorting & searching queries
    """
    # Get all products from db
    products = Product.objects.all()

    # Insert products into context list, which will be passed
    # to the template
    context = {
        'products': products
    }
    return render(request, "products/products.html", context)
