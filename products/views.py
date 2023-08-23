from django.shortcuts import render
from .models import Product


def see_all_products(request):
    """ view returns all the products and handles searching and sorting """

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)
