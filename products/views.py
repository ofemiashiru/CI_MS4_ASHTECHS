from django.shortcuts import render, get_object_or_404
from .models import Product


def see_all_products(request):
    """ view returns all the products and handles searching and sorting """

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)


def see_product_details(request, product_id):
    """ view each product and its details """

    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_details.html', context)

