from django.core.exceptions import ValidationError
from django.db.models import Q
from django.test import TestCase

from app2.models import Product


class ProductTest(TestCase):
    def test_01(self):
        data = {
            'name': 'A',
            'price': 1,
            'content': {
                'name': 'A',
                'price': 1,
            },
        }
        product = Product.objects.create(**data)
        self.assertIsInstance(product, Product)

    def test_02(self):
        data = {
            'name': 'A',
            'description': 'A',
            'price': 1,
            'content': {
                'name': 'A' * 101,
                'description': 'A',
                'price': 1,
            },
        }
        with self.assertRaises(ValidationError):
            Product.objects.create(**data)

    def test_03(self):
        data = {
            'name': 'A',
            'price': 1,
            'content': {
                'name': 'A',
                'price': 1,
            },
        }
        Product.objects.create(**data)
        product = Product.objects.all().first()
        self.assertIsInstance(product.content, dict)

    def test_04(self):
        data = {
            'name': 'A',
            'price': 1,
            'content': {
                'name': 'A',
                'price': 1,
            },
        }
        Product.objects.create(**data)
        q = Q(content__name='A')
        product = Product.objects.filter(q).first()
        self.assertIsInstance(product.content, dict)
