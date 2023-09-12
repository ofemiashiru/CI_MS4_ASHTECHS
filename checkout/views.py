from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

import os

if os.path.exists("env.py"):
    import env


# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, 'There are no items in your bag')
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': os.environ.get('STRIPE_PK'),
        'client_secret': os.environ.get('STRIPE_SECRET_KEY')
    }

    return render(request, template, context)
