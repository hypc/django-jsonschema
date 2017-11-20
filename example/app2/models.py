import uuid

from django.db import models

from django_jsonschema.postgres.models import JSONSchemaField


class Product(models.Model):
    content_schema = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string', 'maxLength': 100},
            'price': {'type': 'integer', 'minimum': 0},
            'description': {'type': 'string', 'maxLength': 300},
            'images': {
                'type': 'array',
                'items': {'type': 'string'}
            }
        },
        'required': ['name', 'price']
    }
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid1)
    name = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    price = models.PositiveIntegerField()
    content = JSONSchemaField(schema=content_schema)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def detail(self):
        return {
            'product_id': self.product_id.hex,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'content': self.content,
            'created_time': self.created_time.timestamp(),
            'updated_time': self.updated_time.timestamp(),
        }
