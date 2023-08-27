from django.shortcuts import (
        render, get_object_or_404, redirect, reverse, HttpResponse)
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def see_all_products(request):
    """ view returns all the products and handles searching and sorting """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']

            if not query:
                messages.error(request, 'No search criteria was entered')
                return redirect(reverse('products'))

            if query:
                queries = Q(
                    name__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)

    context = {
        'products': products,
        'search': query,
        'current_categories': categories
    }

    return render(request, 'products/products.html', context)


def see_all_accessories(request):
    """ view returns all the accessories """

    products = Product.objects.filter(is_accessory=True)
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_categories': categories
    }

    return render(request, 'products/products.html', context)


def see_product_details(request, product_id):
    """ view each product and its details """

    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_details.html', context)
