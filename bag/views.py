from django.shortcuts import render, redirect, reverse, HttpResponse


# Create your views here.
def see_shopping_bag(request):
    """ view returns the shopping bag page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add chosen quantity to the bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)


def update_bag(request, product_id):
    """ Update the quantity of chosen item in the bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[product_id] = quantity
    else:
        bag.pop(product_id)

    request.session['bag'] = bag

    return redirect(reverse('shopping_bag'))


def remove_from_bag(request, product_id):
    """ Removes specific product from shopping bag """

    bag = request.session.get('bag')
    try:
        del bag[product_id]
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
