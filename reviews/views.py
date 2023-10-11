from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse,
    redirect
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from profiles.models import UserProfile
from reviews.models import Review

from reviews.forms import ReviewForm

# Create your views here.


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


@login_required
def add_review(request, product_id):
    """ Allow user to add reviews"""

    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        user = get_object_or_404(UserProfile, user=request.user)
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

                # get the new rating
                this_review = Review.objects.filter(product=product_id)
                new_rating = get_ratings(this_review)

                # add rating to product model
                product.rating = new_rating[int(product_id)]
                product.save(update_fields=['rating'])

                messages.success(request, 'Review succesfully added.')
                return redirect(reverse('product_details', args=[product_id]))

        return render(request, 'reviews/add_review.html', context)
    else:
        messages.info(request, 'You need to be logged in to leave a review.')
        return redirect('products')


@login_required
def update_review(request, review_id):
    """ Allow users to update their review"""

    if request.user.is_authenticated:
        review = get_object_or_404(Review, id=review_id)
        product = get_object_or_404(Product, id=review.product.id)

        if request.method == 'POST':
            if str(review.user_profile) == str(request.user):
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid:
                    form.save()

                    # get the new rating
                    this_review = Review.objects.filter(product=product.id)
                    new_rating = get_ratings(this_review)

                    # add rating to product model
                    product.rating = new_rating[int(product.id)]
                    product.save(update_fields=['rating'])

                    messages.success(request, 'Review succesfully updated.')
                    return redirect(
                        reverse('product_details', args=[product.id])
                    )
            else:
                messages.warning(
                    request, 'You can only update your own reviews.'
                )
        form = ReviewForm(instance=review)

        context = {
            'form': form,
            'product': product,
            'review': review,
            'from_review': True
        }
        return render(request, 'reviews/update_review.html', context)
    else:
        messages.info(request, 'You need to be logged in to update a review.')
        return redirect('products')


@login_required
def delete_review(request, review_id):
    """ Allow users to delete their review """

    if request.user.is_authenticated:
        review = get_object_or_404(Review, id=review_id)
        product = get_object_or_404(Product, id=review.product.id)

        if str(review.user_profile) == str(request.user):
            review.delete()

            # get the new rating
            all_reviews = Review.objects.filter(product=product.id)
            new_rating = get_ratings(all_reviews)

            # add rating to product model
            product.rating = new_rating.get(int(product.id), 0)
            product.save(update_fields=['rating'])

            messages.success(request, 'Review successfully deleted.')

        else:
            messages.warning(request, 'You can only delete your own reviews.')
    else:
        messages.info(request, 'You need to be logged in to delete a review.')

    return redirect(reverse('product_details', args=[product.id]))
