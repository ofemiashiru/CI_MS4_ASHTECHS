from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import stripe
from .models import Order, OrderLineItem
from profiles.models import UserProfile
from products.models import Product
import json
import time


class StripeWebhookHandler:
    """ Class to handle stripe Webhooks """
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Sends confirmation email to user """
        customer_email = order.email

        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        message = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

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
        # save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        # grand_total = round(intent.charges.data[0].amount / 100, 2)

        # for field, value in shipping_details.address.items():
        #     if value == "":
        #         shipping_details.address[field] = None

        # profile = None
        # username = intent.metadata.username

        # if username != 'AnonymousUser':
        #     profile = UserProfile.objects.get(user__username=username)

        #     if save_info:

        #         profile.d_phone_number = shipping_details.phone
        #         profile.d_address_line_1 = shipping_details.address.line1
        #         profile.d_address_line_2 = shipping_details.address.line2
        #         profile.d_city = shipping_details.address.city
        #         profile.d_post_code = shipping_details.address.postal_code
        #         profile.d_country = shipping_details.address.country

        #         profile.save()

        # order_exists = False
        # attempt = 1

        # while attempt <= 5:
        #     try:
        #         order = Order.objects.get(
        #             f_name__iexact=shipping_details.name.split()[0].strip(),
        #             l_name__iexact=shipping_details.name.split()[1].strip(),
        #             email__iexact=billing_details.email,
        #             phone_number__iexact=shipping_details.phone,
        #             address_line_1__iexact=shipping_details.address.line1,
        #             address_line_2__iexact=shipping_details.address.line2,
        #             city__iexact=shipping_details.address.city,
        #             post_code__iexact=shipping_details.address.postal_code,
        #             country__iexact=shipping_details.address.country,
        #             grand_total=grand_total,
        #             original_bag=bag,
        #             stripe_pid=pid,
        #         )

        #         order_exists = True
        #         break

        #     except Order.DoesNotExist():
        #         attempt += 1
        #         time.sleep(1)

        # if order_exists:
        #     self._send_confirmation_email(order)
        #     return HttpResponse(
        #         content=f'Webhook was received: {event["type"]} | Order in Database',
        #         status=200
        #     )
        # else:
        #     order = None
        #     try:
        #         order = Order.objects.create(
        #             f_name=shipping_details.name.split()[0].strip(),
        #             l_name=shipping_details.name.split()[1].strip(),
        #             user_profile=profile,
        #             email=billing_details.email,
        #             phone_number=shipping_details.phone,
        #             address_line_1=shipping_details.address.line1,
        #             address_line_2=shipping_details.address.line2,
        #             city=shipping_details.address.city,
        #             post_code=shipping_details.address.postal_code,
        #             country=shipping_details.address.country,
        #             original_bag=bag,
        #             stripe_pid=pid,
        #         )
        #         for item_id, quantity in json.loads(bag).items():
        #             product = Product.objects.get(id=item_id)
                    
        #             if isinstance(quantity, int):
        #                 order_line_item = OrderLineItem(
        #                     order=order,
        #                     product=product,
        #                     quantity=quantity,
        #                 )
        #                 order_line_item.save()
        #     except Exception as e:
        #         if order:
        #             order.delete()
                    
        #         return HttpResponse(
        #             content=f'Webhook was received: {event["type"]}|Error {e}',
        #             status=500
        #         )

        # self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook was received: {event["type"]}|Success \n {billing_details}\n{shipping_details}\n{pid}\n{bag}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Handle payamnet intent failed webhook """

        return HttpResponse(
            content=f'Webhook was received: {event["type"]}',
            status=200
        )
