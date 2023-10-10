from django.db import models
from products.models import Product
from profiles.models import UserProfile

# Create your models here.


class Wishlist(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=False, blank=False,
        related_name='wishlist'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False
    )
    date = models.DateField(auto_now_add=True)
