from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """ User defualt information """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    d_phone_number = models.CharField(
            max_length=20, null=True, blank=True
        )
    d_address_line_1 = models.CharField(max_length=90, null=True, blank=True)
    d_address_line_2 = models.CharField(max_length=90, null=True, blank=True)
    d_city = models.CharField(max_length=40, null=True, blank=True)
    d_post_code = models.CharField(max_length=20, null=True, blank=True)
    d_country = CountryField(
        blank_label='Country *', max_length=50, null=True, blank=True
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)

    instance.userprofile.save()
