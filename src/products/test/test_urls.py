import pytest
from django.urls import reverse


class TestProductURLs:

    def test_product_list(self):
        url = reverse('products:product-list', args=[])
        assert url == '/products/'

    def test_product_create(self):
        url = reverse('products:product-create')
        assert url == '/products/create/'

    def test_product_detail(self):
        url = reverse('products:product-detail', args=['1'])
        assert url == '/products/1/'

    def test_product_update(self):
        url = reverse('products:product-update', args=['1'])
        assert url == '/products/1/update/'

    def test_product_delete(self):
        url = reverse('products:product-delete', args=['1'])
        assert url == '/products/1/delete/'
