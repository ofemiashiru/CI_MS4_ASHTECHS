from django.shortcuts import (
        render, get_object_or_404, redirect, reverse, HttpResponse,)
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Brand
from reviews.models import Review


def see_all_products(request):
    """ view returns all the products and handles searching and sorting """

    products = Product.objects.all()
    query = None
    categories = None
    brand = None
    sort = None
    direction = None

    if request.GET:

        if 'accessory' in request.GET:
            products = products.filter(is_accessory=True)

        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key

            if sort_key == 'name':
                sort_key = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sort_key == 'brand':
                sort_key = 'brand__name'
            elif sort_key == 'category':
                sort_key = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'

            products = products.order_by(sort_key)

        if 'brandName' in request.GET:
            brand = request.GET['brandName'].split(',')
            products = products.filter(brand__name__in=brand)
            brand = Brand.objects.filter(name__in=brand)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']

            if not query:
                msg = 'No search criteria was entered. Please try again!'
                messages.error(request, msg)
                return redirect(reverse('products'))

            if query:
                queries = Q(
                    name__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'current_brand': brand
    }

    return render(request, 'products/products.html', context)


def see_product_details(request, product_id):
    """ view each product and its details """

    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product_id)

    context = {
        'product': product,
        'reviews': reviews
    }

    return render(request, 'products/product_details.html', context)
