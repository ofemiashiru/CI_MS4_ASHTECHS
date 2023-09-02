from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """ Handles the shopping bag operations """
    bag_items = []
    total = 0
    product_count = 0

    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, id=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'sub_total': product.price * quantity
        })

    if total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE/100)
        free_shipping_difference = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        shipping = 0
        free_shipping_difference = 0

    grand_total = shipping + total

    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'total': total,
        'shipping': shipping,
        'grand_total': grand_total,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'free_shipping_difference': free_shipping_difference
    }

    return context
