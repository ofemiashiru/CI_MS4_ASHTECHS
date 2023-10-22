from django.test import TestCase

from products.models import Product, Brand, Category


class TestViews(TestCase):

    def test_see_all_products(self):
        """test view to see all products"""

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

        template = 'products/products.html'
        self.assertTemplateUsed(response, template)

    def test_see_product_details(self):
        """test view to see product details"""

        brand = Brand.objects.create(
            name='apple',
            friendly_name='Apple'
        )

        category = Category.objects.create(
            name='laptop_computer',
            friendly_name='Laptop'
        )

        product = Product.objects.create(
            name='Test',
            brand=brand,
            category=category,
            is_accessory=False,
            description='Test_Description',
            price=29.99,
            rating=0,
            new_arrival=False,
            deal=False,
            clearance=False
        )

        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)

        template = 'products/product_details.html'
        self.assertTemplateUsed(response, template)
