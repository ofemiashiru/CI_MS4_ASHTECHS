from django.contrib import admin
from .models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):

    fields = (
        'user_profile', 'title', 'review_content', 'product', 'rating',
    )

    list_display = (
        'user_profile', 'product', 'title', 'review_content', 'rating', 'date'
    )

    ordering = ('-date',)


admin.site.register(Review, ReviewAdmin)