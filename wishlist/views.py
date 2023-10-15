from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect
from products.models import Product
from wishlist.models import Wishlist
from profiles.models import UserProfile

from django.contrib import messages


def toggle_wishlist(request, product_id):
    """ Add and remove item from wishlist """

    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        product = get_object_or_404(Product, id=product_id)
        all_wishlist_items = Wishlist.objects.filter(user_profile=user)
        wishlist_item = all_wishlist_items.filter(product=product_id)

        if (wishlist_item):
            wishlist_item.delete()
            messages.success(request, f'{product.name} removed from Wishlist')
        else:
            new_wishlist_item = Wishlist.objects.create(
                user_profile=user, product=product
            )
            new_wishlist_item.save()
            messages.success(request, f'{product.name} added to Wishlist')

    else:
        messages.error(
            request, 'You need to be logged in to complete this action.'
        )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
