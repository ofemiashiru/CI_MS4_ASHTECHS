from django.db import models

from products.models import Product
from profiles.models import UserProfile

# Create your models here.


class Review(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='reviews'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False
    )
    title = models.CharField(max_length=50, null=False, blank=False)
    review = models.CharField(max_length=255, null=False, blank=False)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title