import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product
from profiles.models import UserProfile

from django_countries.fields import CountryField

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='orders'
    )
    f_name = models.CharField(max_length=50, null=False, blank=False)
    l_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(
        max_length=20, null=False, blank=False
    )
    address_line_1 = models.CharField(max_length=90, null=False, blank=False)
    address_line_2 = models.CharField(max_length=90, null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(
        blank_label='Country *', max_length=80, null=False, blank=False
    )
    date = models.DateField(auto_now_add=True)
    shipping_costs = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
    )

    def _generate_order_num(self):
        """ generate random order number """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ update grand total everytime a line_item has been added  """
        self.order_total = (
            self.lineitems.aggregate(
                Sum('line_item_total'))['line_item_total__sum'] or 0
            )
        if self.order_total < settings.FREE_SHIPPING_THRESHOLD:
            self.shipping_costs = (
                self.order_total * settings.STANDARD_SHIPPING_PERCENTAGE / 100
            )
        else:
            self.shipping_costs = 0
        self.grand_total = self.order_total + self.shipping_costs
        self.save()

    def save(self, *args, **kwargs):
        """ set the order number if it has not already been set """

        if not self.order_number:
            self.order_number = self._generate_order_num()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems'
    )

    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_item_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """ set the line item total field overriding it save method """
        self.line_item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'ID {self.product.id} on order {self.order.order_number}'
