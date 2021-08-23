from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):
    """
    View to show all products, sorting & searching queries
    """
    # Get all products from db
    products = Product.objects.all()
    # Initally set query to None to avoid error when loading
    # products page without search term
    query = None
    categories = None

    # If the request is GET, can access seach queries as GET parameters
    # Chech if request.GET exists
    if request.GET:
        # Check if 'category' is in request.GET. 'category' is parameter
        # in URLs for categories in main-nav
        if 'category' in request.GET:
            # If category is present, split it into a list at the comma
            categories = request.GET['category'].split(",")
            # Use the list to filter the queryset of all products to only
            # products whose category name is in the list
            # We're looking for the name field of the category model
            # Can do because category and products are related with foreign key
            # Double underscore syntax allows us to drill into related model
            products = products.filter(category__name__in=categories)
            # Filter all categories down to the ones whose name is in the list
            # from the URL
            categories = Category.objects.filter(name__in=categories)
            # I think what happened here is this:
            # We created a list from the category paramater that was passed in
            # - eg: activewear,essentials became ['activewear', 'essentials']
            # Then, we checked Categories in the db to see if any categories
            # matched that list. Then, we filtered the products down to a list
            # of products who are in that category, saved them to 'products'
            # variable, which is then passed into the context.
            # Then, we filtered down all the categories in the db to the ones
            # whose name is in the list, saved it to 'categories' variable
            # and passed it into the context
            # FOR OWN PROJECT, TRY:
            # Instead of '?category=activewear,essentials', replace 'category'
            # with 'q' and use the below 'q' code.
        # Check if 'q' is in request.GET. Text input in form is named 'q'
        if 'q' in request.GET:
            # If q is present, set it equal to query
            query = request.GET['q']
            # If query is blank, attach error message to the request and
            # redirect back to products URL.
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            # If not, generate search query.
            # First, use Q to ensure the query searches for match
            # in either name OR description because, in Django,
            # if you use filter method, the search term would have to match
            # both name and description
            # 'i' makes the queries case insensitive
            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            # Now that either/or queries are constructed, they can be filtered
            # using the filter method
            products = products.filter(queries)

    # Insert products into context list, which will be passed
    # to the template
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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
