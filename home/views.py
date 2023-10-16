from django.shortcuts import render
from products.models import Product

import random


def index(request):
    """ view returns the index (home) page"""

    products = Product.objects.all()
    number_of_products = len(products)
    product_one = products[random.randrange(number_of_products)]
    product_two = products[random.randrange(number_of_products)]

    context = {
        'product_one': product_one,
        'product_two': product_two
    }

    return render(request, 'home/index.html', context)
