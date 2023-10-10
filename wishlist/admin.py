from django.contrib import admin
from wishlist.models import Wishlist
# Register your models here.


class WishlistAdmin(admin.ModelAdmin):

    list_display = (
        'user_profile',
        'product',
        'date',
    )

    ordering = ('-date',)


admin.site.register(Wishlist, WishlistAdmin)
