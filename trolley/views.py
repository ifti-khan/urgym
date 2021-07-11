from django.shortcuts import render, redirect

# Create your views here.


def view_trolley(request):
    """
    A view that renders the trolley page
    and its contents
    """

    return render(request, 'trolley/trolley.html')


def add_to_trolley(request, item_id):
    """
    Adds a product quantity specified by the user
    to the shopping trolley
    """

    # This block of code gets the quantity from the form and coverts it
    # from string to integer.
    # It also gets the redirect url from the form and then creates a empty
    # trolley dictionary session if one has not already been created.
    quantity = int(request.POST.get('product_quantity'))
    redirect_url = request.POST.get('redirect_url')

    # This block of code initializes the size var to none and then checks
    # to see if the product sizes has been posted to the URL and then
    # sets size to the size selected from the URL
    size = None
    if 'clothing_sizes' in request.POST:
        size = request.POST['clothing_sizes']

    trolley = request.session.get('trolley', {})

    # This block of code will check to see if the same item with the same
    # size is in the trolley and if it is then the quantity will be incremented
    # and if not then set it to the quantity the user has chosen. This only
    # applies to products that have sizes.
    if size:
        if item_id in list(trolley.keys()):
            if size in trolley[item_id]['item_size'].keys():
                trolley[item_id]['item_size'][size] += quantity
            else:
                trolley[item_id]['item_size'][size] = quantity
        else:
            trolley[item_id] = {'item_size': {size: quantity}}
    else:

        # This block of code will update the quantity if the same item is
        # already in the trolley, if not then it will add the item to the
        # shopping trolley and overwrite the session variable with the
        # updated the session and then redirect using the redirect url
        if item_id in list(trolley.keys()):
            trolley[item_id] += quantity
        else:
            trolley[item_id] = quantity

    request.session['trolley'] = trolley
    return redirect(redirect_url)