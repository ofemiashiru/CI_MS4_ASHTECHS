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

    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        user  = get_object_or_404(UserProfile, user=request.user)
        review_form = ReviewForm()

        context = {
            'product': product,
            'review_form': review_form,
            'from_review': True
        }
        if request.method == 'POST':
            form_data = {
                'title': request.POST['title'],
                'review_content': request.POST['review_content'],
                'rating': request.POST['rating'],
            }
            review_form = ReviewForm(form_data)

            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.product_id = product_id
                review.user_profile = user
                review.save()

                messages.success(request, 'Review succesfully added')
                return render(request, 'reviews/add_review.html', context)


        return render(request, 'reviews/add_review.html', context)

    messages.info(request, 'You need to be logged in to leave a review')
    return redirect('products')
