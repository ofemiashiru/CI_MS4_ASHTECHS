from django.http import HttpResponse
import stripe
from .models import Order, OrderLineItem
import json


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

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        order_exists = False
        try:
            order = Order.objects.get(
                f_name__iexact=shipping_details.f_name,
                l_name__iexact=shipping_details.l_name,
                email__iexact=shipping_details.email,
                phone_number__iexact=shipping_details.phone,
                address_line_1__iexact=shipping_details.line_1,
                address_line_2__iexact=shipping_details.line_2,
                city__iexact=shipping_details.city,
                post_code__iexact=shipping_details.postal_code,
                country__iexact=shipping_details.country,
                grand_total=shipping_details.grand_total,
            )

            order_exists = True
            return HttpResponse(
                content=f'Webhook was received: {event["type"]} \
                | Order in Database',
                status=200
            )

        except Order.DoesNotExist():
            try:
                for item_id, quantity in json.loads(bag).items():
                    order = Order.objects.create(
                        f_name=shipping_details.f_name,
                        l_name=shipping_details.l_name,
                        email=shipping_details.email,
                        phone_number=shipping_details.phone,
                        address_line_1=shipping_details.line_1,
                        address_line_2=shipping_details.line_2,
                        city=shipping_details.city,
                        post_code=shipping_details.postal_code,
                        country=shipping_details.country,
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
            content=f'Webhook was received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Handle payamnet intent failed webhook """

        return HttpResponse(
            content=f'Webhook was received: {event["type"]}',
            status=200
        )
