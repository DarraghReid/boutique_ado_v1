from decimal import Decimal
from django.conf import settings


# This function is a context processor. Its purpose is the make
# this context dictionary available to all templates in entire application
# Like request.user in any template because of built in request context
# processor.
# Add it to list of context processors in templates variable in settings.py
def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

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
