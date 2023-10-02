from django.http import HttpResponse
import stripe
from .models import Order, OrderLineItem
from products.models import Product
import json
import time


class StripeWebhookHandler:
    """ Class to handle stripe Webhooks """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle general, unknown or unexpected webhook """
        return HttpResponse(
            content=f'Unhandled webhook was received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handle payamnet intent succeeded webhook """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        order_exists = False
        attempt = 1

        while attempt <= 5:
            try:
                order = Order.objects.get(
                    f_name__iexact=shipping_details.name.split()[0].strip(),
                    l_name__iexact=shipping_details.name.split()[1].strip(),
                    email=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    address_line_1__iexact=shipping_details.address.line1,
                    address_line_2__iexact=shipping_details.address.line2,
                    city__iexact=shipping_details.address.city,
                    post_code__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    grand_total=shipping_details.grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )

                order_exists = True
                break

            except Order.DoesNotExist():
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook was received: {event["type"]} \
                | Order in Database',
                status=200
            )
        else:
            order = None
            try:
                for item_id, quantity in json.loads(bag).items():
                    order = Order.objects.create(
                        f_name=shipping_details.name.split()[0],
                        l_name=shipping_details.name.split()[1],
                        email=billing_details.email,
                        phone_number=shipping_details.phone,
                        address_line_1=shipping_details.address.line1,
                        address_line_2=shipping_details.address.line2,
                        city=shipping_details.address.city,
                        post_code=shipping_details.address.postal_code,
                        country=shipping_details.address.country,
                        original_bag=bag,
                        stripe_pid=pid,
                    )

                    product = Product.objects.get(id=item_id)

                    if isinstance(quantity, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook was received: {event["type"]}|Error {e}',
                    status=500
                )

        return HttpResponse(
            content=f'Webhook was received: {event["type"]}|Success',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Handle payamnet intent failed webhook """

        return HttpResponse(
            content=f'Webhook was received: {event["type"]}',
            status=200
        )