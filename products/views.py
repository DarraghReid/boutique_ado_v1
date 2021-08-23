from django.shortcuts import render, get_object_or_404
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
        'products': products,
    }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """
    View to show individual product details
    """
    # Find product in db, by setting Primary Key to product id
    product = get_object_or_404(Product, pk=product_id)

    # Insert products into context list, which will be passed
    # to the template
    context = {
        'product': product,
    }
    return render(request, "products/product_detail.html", context)
