from django.db import models


# Caterory model will inherit from models.Model
# (models in imported above from django.db)
class Category(models.Model):
    # Name is a character field that represents the programatic name,
    # which will make it easier to find in views and other code etc
    name = models.CharField(max_length=254)
    # More friendly name for front end
    # Null in db and blank in forms so that it is optional
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # String method takes in the category model itself
    # returns the name variable
    # __str__ methods seem to be just a string representation of the
    # class/object
    def __str__(self):
        return self.name

    # Model method does same as __str__ method, except returns
    # friendly name
    def get_friendly_name(self):
        return self.friendly_name


# Product model
# Each model requires a name, description and price, all else is optional
class Product(models.Model):
    # Null in Categories, Blank in forms, and if a category is deleted,
    # set any products that use it to have null for this field,
    # rather than delete the product
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # String method
    def __str__(self):
        return self.name
