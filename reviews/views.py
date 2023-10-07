from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def add_review(request, product_id):

    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)

        context = {
            'product': product
        }
        return render(request, 'reviews/add_review.html', context)

    messages.info(request, 'You need to be logged in to leave a review')
    return redirect('products')
