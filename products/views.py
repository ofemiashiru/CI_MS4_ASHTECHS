from django.shortcuts import (
        render, get_object_or_404, redirect, reverse)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Brand
from reviews.models import Review
from wishlist.models import Wishlist
from profiles.models import UserProfile
from .forms import ProductForm


def see_all_products(request):
    """ view returns all the products and handles searching and sorting """

    # Brings back all the wishlist items for user
    wishlist_product_ids = []
    if str(request.user) != 'AnonymousUser':
        user = get_object_or_404(UserProfile, user=request.user)
        all_wishlist_items = Wishlist.objects.filter(user_profile=user)

        for item in all_wishlist_items.values():
            if item['product_id']:
                wishlist_product_ids.append(item['product_id'])

    products = Product.objects.all()
    query = None
    categories = None
    brand = None
    sort = None
    direction = None
    other_filter = None

    if request.GET:

        if 'accessory' in request.GET:
            products = products.filter(is_accessory=True)
            other_filter = 'accessory'

        if 'new_arrival' in request.GET:
            products = products.filter(new_arrival=True)
            other_filter = 'new_arrival'

        if 'deals' in request.GET:
            products = products.filter(deal=True)
            other_filter = 'deals'

        if 'clearance' in request.GET:
            products = products.filter(clearance=True)
            other_filter = 'clearance'

        if 'all_specials' in request.GET:
            products = products.filter(
                Q(clearance=True) | Q(deal=True) | Q(new_arrival=True)
            )
            other_filter = 'all_specials'

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

    paginator = Paginator(products, 16)
    page_number = request.GET.get("page")

    products_page_obj = paginator.get_page(page_number)

    context = {
        'products': products_page_obj,
        'wishlist_product_ids': wishlist_product_ids,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'current_brand': brand,
        'other_filter_url': f'&{other_filter}=true' if other_filter else '',
        'current_sort_url': (
            f'&sort={sort}&direction={direction}' if sort else ''
        )
    }

    return render(request, 'products/products.html', context)


def see_product_details(request, product_id):
    """ view each product and its details """

    # Brings back all the wishlist items for user
    wishlist_product_ids = []
    if str(request.user) != 'AnonymousUser':
        user = get_object_or_404(UserProfile, user=request.user)
        all_wishlist_items = Wishlist.objects.filter(user_profile=user)

        for item in all_wishlist_items.values():
            if item['product_id']:
                wishlist_product_ids.append(item['product_id'])

    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product_id)

    context = {
        'product': product,
        'reviews': reviews,
        'wishlist_product_ids': wishlist_product_ids,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """ Add product to store """

    if request.user.is_superuser:

        if request.method == 'POST':
            product_form = ProductForm(request.POST, request.FILES)
            if product_form.is_valid():
                product = product_form.save()
                messages.success(request, 'Product added successfully.')

                return redirect(reverse('product_details', args=[product.id]))
            else:
                messages.error(
                    request, 'Product could not be added, try again.'
                )
        else:
            product_form = ProductForm()

        context = {
            'product_form': product_form
        }

        return render(request, 'products/add_product.html', context)
    else:
        messages.info(request, 'You are not able to access this page.')
        return redirect(reverse('home'))


@login_required
def edit_product(request, product_id):
    """ Edit product in store """

    if request.user.is_superuser:

        product = get_object_or_404(Product, id=product_id)
        current_rating = product.rating

        if request.method == 'POST':

            product_form = ProductForm(
                request.POST, request.FILES, instance=product
            )

            if product_form.is_valid():
                product_form.save()

                product.rating = current_rating
                product.save(update_fields=['rating'])

                messages.success(request, 'Product update successfully.')
                return redirect(reverse('product_details', args=[product_id]))
            else:
                messages.error(
                    request, 'Product not updated. Please try again.'
                )

        else:
            product_form = ProductForm(instance=product)

        context = {
            'product_form': product_form,
            'product': product
        }

        return render(request, 'products/edit_product.html', context)

    else:
        messages.info(request, 'You are not able to access this page.')
        return redirect(reverse('home'))


@login_required
def delete_product(request, product_id):
    """ delete product from store"""
    if request.user.is_superuser:

        product = get_object_or_404(Product, id=product_id)

        product.delete()
        messages.success(request, 'Product deleted successfully.')

    else:
        messages.info(request, 'You are not able to access this page.')

    return redirect(reverse('products'))
