from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


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
        'stripe_public_key': 'pk_test_51Nn7NvClUCnFaeZaRDqrXMnJFRkDvWvzGytM0LMdBK4MBFtFtHclrbRU1rnYdGeCfRi2lq5o99NA7W2YnVyTw4It00xlbnuJF2',
        'client_secret': 'the-secret-key'
    }

    return render(request, template, context)
