from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse,
    redirect
)
from django.contrib import messages

from products.models import Product
from profiles.models import UserProfile
from reviews.models import Review

from reviews.forms import ReviewForm

# Create your views here.


def add_review(request, product_id):
    profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=profile)

        if review_form.is_valid():
            review_form.save()

            messages.success(request, 'Review succesfully added')
            return HttpResponse('Posted')
                

    if request.user.is_authenticated:

        review_form = ReviewForm()

        context = {
            'product': product,
            'review_form': review_form,
            'from_review': True
        }
        return render(request, 'reviews/add_review.html', context)

    messages.info(request, 'You need to be logged in to leave a review')
    return redirect('products')
