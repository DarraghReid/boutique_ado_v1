from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

# Create your views here.


def all_products(request):
    """
    View to show all products, sorting & searching queries
    """
    # Get all products from db
    # Objects refers to all products under products in db
    products = Product.objects.all()
    # Initally set query to None to avoid error when loading
    # products page without search term
    query = None
    # Initally set categories to None to avoid error when loading
    # products page without search term
    categories = None
    sort = None
    direction = None

    # If the request is GET, can access seach queries as GET parameters
    # Check if request.GET exists
    if request.GET:
        # If the requests GET parameters contain 'sort':
        if 'sort' in request.GET:
            # Set sortkey equal to value of sort (None atm)
            sortkey = request.GET['sort']
            # Set sort from None to sortkey
            sort = sortkey
            # check to see if sortkey is equal to 'name'
            # It seems the reason we copies sort param into sortkey
            # is to preserve the the original field name ("name"),
            # while we opperate on lower_name field
            if sortkey == "name":
                # Set it to lower_name
                sortkey = 'lower_name'
                # lower_name is temporary field of all prdct names in lwr-case
                products = products.annotate(lower_name=Lower('name'))

            # Ensure categories are sorted by names
            if sortkey == 'category':
                # Drill into related model with double underscore
                sortkey == 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Check if 'category' is in request.GET. 'category' is parameter
        # in URLs for categories in main-nav
        if 'category' in request.GET:
            # If category is present, split it into a list at the comma
            categories = request.GET['category'].split(",")
            # Use the list to filter the queryset of all products to only
            # products whose category name is in the list.
            # We're looking for the name field of the category model
            # Can do because category and products are related with foreign key
            # Double underscore syntax allows us to drill into related model
            # Basically, here, we're accessing the category field/name of each
            # product and matching it with the category/categories in the list
            # If they match, the product is saved to 'products' below
            # and passed to the context.
            products = products.filter(category__name__in=categories)
            # Filter all categories down to the ones whose name is in the list
            # from the URL. This time, instead of accessing a product's
            # category name, we're going straight into the Category model
            # (Category in db), filtering its objects (categories) by name,
            # and matching them to categories in the list. If they match, the
            # category is saved to 'categories' below and passed to context.
            categories = Category.objects.filter(name__in=categories)
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

    current_sorting = f'{sort}_{direction}'

    # Insert products into context list, which will be passed
    # to the template
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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
