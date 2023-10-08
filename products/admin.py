from django.contrib import admin
from products.models import Brand, Category, Product

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):

    readonly_fields = ('rating',)

    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
        'is_accessory',
    )

    ordering = ('price',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
