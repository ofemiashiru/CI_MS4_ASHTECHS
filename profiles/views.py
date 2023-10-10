from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order, OrderLineItem
from products.models import Product
from wishlist.models import Wishlist


@login_required
def profile(request):
    """ Show Users profile """
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist_items = Wishlist.objects.filter(user_profile=profile)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            success_message = 'Your profile has been updated'
            messages.success(request, success_message)
        else:
            messages.error(request, 'Could not update profile. \
                Please try again.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'wishlist_items': wishlist_items,
        'on_profile': True
    }
    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):
    """ link to order history """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, f'Order history for order {order.order_number}')

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)
