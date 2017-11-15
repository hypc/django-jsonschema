import unittest

from django.core.exceptions import ValidationError

from django_jsonschema.forms import JSONSchemaField


class JSONSchemaFieldTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "price": {"type": "number", "multipleOf": 0.01}
            },
            "required": ["name", "price"]
        }
        cls.field = JSONSchemaField(schema)

    def test_1(self):
        value = self.field.clean('{"name": "A", "price": 0.2}')
        self.assertEqual(value['name'], 'A')
        self.assertEqual(value['price'], 0.2)

    def test_2(self):
        value = self.field.clean('{"name": "A", "price": 0.02}')
        self.assertEqual(value['name'], 'A')
        self.assertEqual(value['price'], 0.02)

    def test_3(self):
        with self.assertRaises(ValidationError):
            self.field.clean('{"name": 1, "price": 0.02}')

    def test_4(self):
        with self.assertRaises(ValidationError):
            self.field.clean('{"name": "1", "price": 0.002}')

    def test_5(self):
        with self.assertRaises(ValidationError):
            self.field.clean('{"name": "1"}')
