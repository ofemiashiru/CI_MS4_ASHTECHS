from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.db.models import Q

import random


def index(request):
    """ view returns the index (home) page"""
    product_one = Product.objects.filter(Q(clearance=True) & Q(is_accessory=False)).first()
    product_two = Product.objects.filter(Q(deal=True) & Q(is_accessory=True)).last()

    context = {
        'product_one': product_one,
        'product_two': product_two
    }

    return render(request, 'home/index.html', context)
