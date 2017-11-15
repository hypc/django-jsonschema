from django.core.exceptions import ValidationError
from django.test import TestCase

from app.models import Product


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
        Product.objects.create(**data)

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
