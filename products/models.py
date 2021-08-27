from django.db import models


# Category model will inherit from models.Model
# (models in imported above from django.db)
class Category(models.Model):

    # Meta class to correct spelling in Admin
    # No need to migrate specifically for this as it does not
    # change the structure of the model
    class Meta:
        verbose_name_plural = "Categories"

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
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # String method
    def __str__(self):
        return self.name
