from django import forms

from django_json_schema.forms import JSONSchemaField
from .models import Product


class ProductCreateForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=300)
    price = forms.IntegerField(min_value=0)
    content = JSONSchemaField(schema=Product.content_schema)
