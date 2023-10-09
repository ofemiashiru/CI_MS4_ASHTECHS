from django import forms

from .models import Product, Category, Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_friendly_names = [
            (c.id, c.get_friendly_name()) for c in categories
        ]

        brands = Brand.objects.all()
        brand_friendly_names = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['category'].choices = category_friendly_names
        self.fields['brand'].choices = brand_friendly_names
