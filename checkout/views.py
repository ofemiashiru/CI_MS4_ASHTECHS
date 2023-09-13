from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from bag.contexts import bag_contents

from products.models import Product
from checkout.models import Order, OrderLineItem

import stripe

import os

if os.path.exists("env.py"):
    import env


# Create your views here.


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
            order = order_form.save()

            for item_id, quantity in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    print(isinstance(quantity, int))
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

            request.session['save_info'] = 'save_info' in request.POST

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

    if not stripe_public_key:
        messages.warning(request, 'Something went wrong! Public key missing.')

    order_form = OrderForm
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

    messages.success(request, f'Your order has been succesfull.\n \Your order \
        number is {order_number}. \n\n Confirmation of your order will \
            be sent to {order.email}'
        )

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'

    context = {
        'order': order
    }
    return render(request, template, context)
