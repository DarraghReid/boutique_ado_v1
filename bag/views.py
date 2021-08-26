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

    # Session allows info to be stoned until client are server are
    # done communicating. Allows us to store contents of shopping bag
    # in http session, allowing users to browse site, add items to bag
    # Session allows bag to persist until user closes browser

    # 'bag' accesses request's session, tries to get variable if it
    # already exists, initialises it to emtpy dictionary if not
    bag = request.session.get('bag', {})

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
