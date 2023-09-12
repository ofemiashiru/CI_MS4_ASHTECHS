from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

from pathlib import Path
import os

if os.path.exists("env.py"):
    import env


# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, 'There are no items in your bag')
        return redirect(reverse('products'))

    order_form = OrderForm
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': os.environ.get('STRIPE_PK'),
        'client_secret': os.environ.get('STRIPE_SECRET_KEY')
    }

    return render(request, template, context)
