from django.test import TestCase
from django.contrib.auth.models import User

from products.models import Product, Brand, Category
from reviews.models import Review


class TestViews(TestCase):

    def test_add_review_get(self):
        """ test view for adding a review get request """

        self.brand = Brand.objects.create(
            name='google',
            friendly_name='Google'
        )

        self.category = Category.objects.create(
            name='laptop_computer',
            friendly_name='Laptop'
        )

        self.product = Product.objects.create(
            name='Test',
            brand=self.brand,
            category=self.category,
            is_accessory=False,
            description='Test_Description',
            price=29.99,
            rating=0,
            new_arrival=False,
            deal=False,
            clearance=True
        )

        self.user = User.objects.create_user(
            username='phife',
            password='aTribeCalledQuest'
        )

        self.client.login(username='phife', password='aTribeCalledQuest')

        response = self.client.get(f'/reviews/add_review/{self.product.id}')
        self.assertEquals(response.status_code, 200)

        template = 'reviews/add_review.html'
        self.assertTemplateUsed(response, template)

    def test_add_update_delete_review(self):
        """ test view for adding, updating and deleting a review """

        self.brand = Brand.objects.create(
            name='google',
            friendly_name='Google'
        )

        self.category = Category.objects.create(
            name='laptop_computer',
            friendly_name='Laptop'
        )

        self.product = Product.objects.create(
            name='Test',
            brand=self.brand,
            category=self.category,
            is_accessory=False,
            description='Test_Description',
            price=29.99,
            rating=0,
            new_arrival=False,
            deal=False,
            clearance=True
        )

        self.user = User.objects.create_user(
            username='phife',
            password='aTribeCalledQuest'
        )

        self.client.login(username='phife', password='aTribeCalledQuest')

        response = self.client.post(f'/reviews/add_review/{self.product.id}', {
            'title': 'A good product',
            'review_content': 'This product is very good',
            'rating': 90,
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(
            Review.objects.get(id=self.product.id).title, 'A good product'
        )

        response_update = self.client.post(
            f'/reviews/update_review/{self.product.id}', {
                'title': 'Could be better',
                'review_content': 'This product is very good',
                'rating': 2,
            })

        self.assertEquals(response_update.status_code, 302)
        self.assertEquals(Review.objects.get(id=self.product.id).rating, 2)

        self.client.get(f'/reviews/delete_review/{self.product.id}')

        with self.assertRaises(Review.DoesNotExist):
            Review.objects.get(id=self.product.id)
