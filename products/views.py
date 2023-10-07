from django.shortcuts import (
        render, get_object_or_404, redirect, reverse, HttpResponse,)
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Brand
from reviews.models import Review


def get_ratings(model):
    """
    Get ratings for each product and does average calculations
    """
    rating_dict = {}
    for review in model:
        if review.product.id not in rating_dict:
            rating_dict[review.product.id] = [int(review.rating)]
        else:
            rating_dict[review.product.id].append(int(review.rating))

    sum_of_rating_dict = {}
    for key, value in rating_dict.items():
        sum_of_rating_dict[key] = int(sum(value)/len(rating_dict[key]))

    return sum_of_rating_dict


def see_all_products(request):
    """ view returns all the products and handles searching and sorting """

    products = Product.objects.all()
    reviews = Review.objects.all()
    query = None
    categories = None
    brand = None
    sort = None
    direction = None

    if request.GET:

        if 'accessory' in request.GET:
            products = products.filter(is_accessory=True)

        if 'new_arrival' in request.GET:
            products = products.filter(new_arrival=True)

        if 'deals' in request.GET:
            products = products.filter(deal=True)

        if 'clearance' in request.GET:
            products = products.filter(clearance=True)

        if 'all_specials' in request.GET:
            products = products.filter(
                Q(clearance=True) | Q(deal=True) | Q(new_arrival=True)
            )

        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            
            # Create a separate action for rating as it is not stored in DB
            if sort_key == 'rating':
                all_ratings = get_ratings(reviews)
                print("REACHED")
                print(all_ratings)
            else:
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

    ratings = get_ratings(reviews)

    context = {
        'products': products,
        'ratings': ratings,
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

    ratings = get_ratings(reviews)

    context = {
        'product': product,
        'reviews': reviews,
        'ratings': ratings
    }

    return render(request, 'products/product_details.html', context)
