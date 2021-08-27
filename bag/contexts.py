from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


# This function is a context processor. Its purpose is the make
# this context dictionary available to all templates in entire application
# Like request.user in any template because of built in request context
# processor.
# Add it to list of context processors in templates variable in settings.py
def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    # Get bag if it exists, initialize it if not
    bag = request.session.get('bag', {})

    # Iterate through all items in shopping bag
    # Get total cost & product count
    # Add products & data to bag items list
    # If item has no sizes, item_data is its quantity
    # If it does, item_data will be dict of items by size
    for item_id, item_data in bag.items():
        # Check if item has sizes by checking if item_data is integer
        # (If it has an integer, item_data is its quantity, therefore,
        # it has no sizes, as explained just above)
        if isinstance(item_data, int):
            # If it does, get the item from the Product
            # model using the item_id as Primary Key
            product = get_object_or_404(Product, pk=item_id)
            # Add product's quantity + price to total
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                "item_id": item_id,
                "quantity": item_data,
                "product": product,
            })
        else:
            # If the item has sizes, get the item from the Product
            # model using the item_id as Primary Key
            product = get_object_or_404(Product, pk=item_id)
            # Iterate through every size of the item
            for size, quantity in item_data['items_by_size'].items():
                # Incremet total price
                total += quantity * product.price
                # Incremet product count
                product_count += quantity
                bag_items.append({
                    "item_id": item_id,
                    "quantity": item_data,
                    "product": product,
                    "size": size,
                })

    # If total is less than FREE_DELIVERY_THRESHOLF in settings.py
    if total < settings.FREE_DELIVERY_THRESHOLD:
        # Then delivery will be total times STANDARD_DELIVERY_PERCENTAGE
        # in settings.py. Wrapped in Decimal funtion impored above
        # Use decimal instead of float as float subject to rounding errors
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # How much more customer needs to spend for free delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    # Everything in the context will be available in every template
    # in every app across entire project
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
