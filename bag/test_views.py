from django.test import TestCase
from django.shortcuts import reverse, redirect
from products.models import Product, Brand, Category


class TestViews(TestCase):

    def test_see_shopping_bag(self):
        """ test view for shopping bag """
        response = self.client.get('/bag/')
        self.assertEquals(response.status_code, 200)

        template = 'bag/bag.html'
        self.assertTemplateUsed(response, template)
