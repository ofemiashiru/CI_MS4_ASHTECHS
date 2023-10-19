from django.db import models

from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=False,
        blank=False, related_name='reviews'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False
    )
    title = models.CharField(max_length=50, null=False, blank=False)
    review_content = models.CharField(max_length=255, null=False, blank=False)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
