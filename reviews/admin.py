from django.contrib import admin
from .models import Review

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):

    readonly_fields = ('rating',)

    fields = (
        'user_profile', 'title', 'review_content', 'product', 'rating',
    )

    list_display = (
        'title', 'review_content', 'rating', 'product', 'user_profile', 'date'
    )

    ordering = ('-date',)


admin.site.register(Review, ReviewAdmin)
