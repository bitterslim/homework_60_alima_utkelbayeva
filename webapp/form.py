from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Product, Cart
from webapp.models.order import Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'leftover', 'price')
        labels = {
            'name': 'Name',
            'description': 'Description',
            'image': 'Image',
            'category': 'Category',
            'leftover': 'Leftover',
            'price': 'Price'
        }

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Find')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user_name', 'phone', 'address')


