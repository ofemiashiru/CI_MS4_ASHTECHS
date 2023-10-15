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

        try:
            order = Order.objects.get(stripe_pid__iexact=pid)
            if order:
                self._send_confirmation_email(order)
                return HttpResponse(
                    content=(
                        f'Webhook was received: \
                        {event["type"]}|Success\n {pid}'
                    ),
                    status=200
                )
        except order.DoesNotExist as e:

            return HttpResponse(
                content=f'Webhook was received: {event["type"]}|Error {e}',
                status=500
            )

    def handle_payment_intent_payment_failed(self, event):
        """ Handle payamnet intent failed webhook """

        return HttpResponse(
            content=f'Webhook was received: {event["type"]}',
            status=200
        )
