from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    # Url for product_detail view in views.py, which contains
    # product id
    path('<product_id>', views.product_detail, name="product_detail"),
]
