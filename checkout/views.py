from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from bag.contexts import bag_contents

from products.models import Product
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

from django.core.mail import send_mail
from django.template.loader import render_to_string


import stripe
import json

import os

if os.path.exists("env.py"):
    import env


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Your payment Cannot be processed. \
            Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):

    stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY')
    stripe_secret_key = os.environ.get('STRIPE_SECRET_KEY')

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'f_name': request.POST['f_name'],
            'l_name': request.POST['l_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'city': request.POST['city'],
            'post_code': request.POST['post_code'],
            'country': request.POST['country']
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, quantity in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(quantity, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )

                        order_line_item.save()

                except Product.DoesNotExist:
                    msg = 'One of the items was not found! Please contact us\
                        for further assistance.'
                    messages.error(request, msg)
                    order.delete()
                    return redirect(reverse('shopping_bag'))

            request.session['save_info'] = 'save-info' in request.POST

            return redirect(
                reverse('checkout_success', args=[order.order_number])
            )
        else:
            messages.error(request, 'Please check you have entered all \
                details in the form correctly')
    else:
        bag = request.session.get('bag', {})
        if not bag:

            messages.error(request, 'There are no items in your bag')
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']

        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'f_name': profile.user,
                    'email': profile.user.email,
                    'phone_number': profile.d_phone_number,
                    'address_line_1': profile.d_address_line_1,
                    'address_line_2': profile.d_address_line_2,
                    'city': profile.d_city,
                    'post_code': profile.d_post_code,
                    'country': profile.d_country,
                })

            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Something went wrong! Public key missing.')

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ Feedback to user if their order has been successful """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'd_phone_number': order.phone_number,
                'd_address_line_1': order.address_line_1,
                'd_address_line_2': order.address_line_2,
                'd_city': order.city,
                'd_post_code': order.post_code,
                'd_country': order.country,
            }

            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(
        request, f'Your order has been succesfull. Your order \
        number is {order_number}. Confirmation of your  \
        order will be sent to {order.email}'
    )

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'

    context = {
        'order': order
    }
    return render(request, template, context)
