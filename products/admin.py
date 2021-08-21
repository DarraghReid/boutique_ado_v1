from django.contrib import admin
from .models import Product, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # List_display attribute is a tuple which tells the
    # admin which fields to display
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    # Sort products by Sku using ordering attribute
    # Has to be a tuple because it's possible to sort
    # on multipe columns
    # To reverse it, add a "-" in front of sku
    ordering = ('sku', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Register admin classes along with their respective models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
