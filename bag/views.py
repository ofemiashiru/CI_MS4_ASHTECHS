from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


def see_shopping_bag(request):
    """ view returns the shopping bag page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add chosen quantity to the bag """

    product = get_object_or_404(Product, id=product_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    plural = '\'s' if quantity > 1 else ''

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
        msg = f'You have {bag[product_id]} "{product}{plural}" in your bag!'
        messages.success(request, msg)
    else:
        bag[product_id] = quantity
        msg = f'You added {bag[product_id]} "{product}{plural}" to your bag!'
        messages.success(request, msg)

    request.session['bag'] = bag

    return redirect(redirect_url)


def update_bag(request, product_id):
    """ Update the quantity of chosen item in the bag """

    product = get_object_or_404(Product, id=product_id)

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    plural = '\'s' if quantity > 1 else ''

    if quantity > 0:
        bag[product_id] = quantity
        msg = f'You have {bag[product_id]} "{product}{plural}" in your bag!'
        messages.success(request, msg)
    else:
        bag.pop(product_id)
        msg = f'You successfully removed "{product}" from your bag!'
        messages.success(request, msg)

    request.session['bag'] = bag

    return redirect(reverse('shopping_bag'))


def remove_from_bag(request, product_id):
    """ Removes specific product from shopping bag """
    product = get_object_or_404(Product, id=product_id)
    bag = request.session.get('bag')

    try:
        del bag[product_id]
        msg = f'You successfully removed "{product}" from your bag!'
        messages.success(request, msg)
        if len(bag) == 0:
            msg = 'Your shopping bag is empty'
            messages.info(request, msg)
        request.session['bag'] = bag
        return redirect(reverse('shopping_bag'))
    except Exception as e:
        messages.error = f'{e}'
        return redirect(reverse('shopping_bag'))
