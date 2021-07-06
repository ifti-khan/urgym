from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):
    """
    A view to show all products on the products page,
    and this also includes sorting products and searching
    for products.
    """
    products = Product.objects.all()
    query = None
    categories = None

    # This block of code is checking if the request get exists,
    # then splits the at the commas to make a list and uses that
    # list to filter the products using the category name from the list
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__category_name__in=categories)
            categories = Category.objects.filter(category_name__in=categories)

    # This block of code is checking if the request get exists
    # and uses the search bar name search and assigns to var query
    # so that it can be used to search for a product within the
    # products db. A error message will display if no search word has
    # been entered and redirected back to the products page.
    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(
                    request, "Please type something to search")
                return redirect(reverse('products'))

            # This block of code uses the user search query and finds
            # a match to the search query in both the
            # product name and description which is case insensitive
            queries = Q(product_name__icontains=query) | Q(
                product_description__icontains=query)
            products = products.filter(queries)

    # context dictionary with keys and values to be
    # used in the rendered html template
    context = {
        'products': products,
        'product_search': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """
    A view to show individual product details
    when a product card is clicked on
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
