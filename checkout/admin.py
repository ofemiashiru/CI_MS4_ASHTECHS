from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInLine(admin.TabularInline):
    """ class to add and edit line items in the admin from the order model """
    model = OrderLineItem
    readonly_fields = ('line_item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,)

    readonly_fields = (
        'order_number',
        'date', 'shipping_costs', 'order_total', 'grand_total'
    )

    fields = (
        'order_number', 'date', 'f_name', 'l_name',
        'email', 'phone_number', 'address_line_1', 'address_line_2',
        'city', 'post_code', 'country', 'shipping_costs', 'order_total',
        'grand_total'
    )

    list_display = (
        'order_number', 'date', 'f_name', 'l_name',
        'shipping_costs', 'order_total', 'grand_total'
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
