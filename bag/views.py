from django.shortcuts import render, redirect


def view_bag(request):
    """
    View to render shopping bag contents page
    """

    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """ Add quantity of specified product to the bag """

    # Get the quantity from the form, convert it to an integer
    quantity = int(request.POST.get('quantity'))

    # Get redirect URL from form so we can redirect back to same URL
    redirect_url = request.POST.get('redirect_url')

    # Set size to None initially
    size = None
    # If product_size is in request.POST, assign it to size
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Session allows info to be stoned until client are server are
    # done communicating. Allows us to store contents of shopping bag
    # in http session, allowing users to browse site, add items to bag
    # Session allows bag to persist until user closes browser

    # 'bag' accesses request's session, tries to get variable if it
    # already exists, initialises it to emtpy dictionary if not
    bag = request.session.get('bag', {})

    # Check if a product with sizes is being added.
    if size:
        # If item is already in bag
        if item_id in list(bag.keys()):
            # Check if another item with same size/id already exists
            if size in bag[item_id]['items_by_size'].keys():
                # If it does, increment the quantity
                bag[item_id]['items_by_size'][size] += quantity
            else:
                # If it doesn't, assign it to quantity. For example,
                # if that item doesn't have any size Ms in the bag,
                # assign that quantity to size M.
                # Already exists in the bag, but this is new size for that item
                bag[item_id]['items_by_size'][size] = quantity
        else:
            # If item is not already in bag, add as dictionary in case
            # we have multiple items with same id, but diff sizes
            # So, items_by_size will track one item, size: quantity
            # will track the number of that item in each size
            bag[item_id] = {'items_by_size': {size: quantity}}
    # If a product with no sizes is being added
    else:
        # Put product & quantity into bag dictionary
        # If item_id already in bag, increment it with quantity
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        # Otherwise, create the key and assign it to quantity
        else:
            bag[item_id] = quantity

    # Put bag variable into session dictionary
    request.session['bag'] = bag

    # Redirect user back to same url
    return redirect(redirect_url)
