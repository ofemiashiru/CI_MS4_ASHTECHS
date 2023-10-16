from django.shortcuts import render
from products.models import Product

import random


def index(request):
    """ view returns the index (home) page"""

    products = Product.objects.all()
    number_of_products = len(products)
    num_arr = []

    while len(num_arr) < 2:
        num = random.randrange(number_of_products)
        if num not in num_arr:
            num_arr.append(num)

    product_one = products[num_arr[0]]
    product_two = products[num_arr[1]]

    context = {
        'product_one': product_one,
        'product_two': product_two
    }

    return render(request, 'home/index.html', context)
