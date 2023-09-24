from django.http import HttpResponse


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