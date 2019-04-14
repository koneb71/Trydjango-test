from django.shortcuts import get_object_or_404
from products.views import *
import pytest

from products.models import Product, ProductCondition

from products.forms import ProductForm

pytestmark = pytest.mark.django_db


class TestProductViews:
    def new_product(self):
        condition = ProductCondition.objects.create(code="N", description="New")
        product = Product.objects.create(title="Sample", price=500, condition=condition)
        return product

    def test_view_product_create(self, rf):
        ProductCondition.objects.create(code="N", description="New")
        data = dict(
            title="Sample product",
            description="Sample Description",
            price=500,
            condition="N"
        )
        request = rf.post('/products/create/', data)

        response = product_create_view(request)
        assert response.status_code == 200

    def test_view_product_list(self, rf):
        request = rf.get('/products/')
        response = product_list_view(request)
        assert response.status_code == 200

    def test_view_product_detail(self, rf):
        product = self.new_product()

        request = rf.post('/products/%s/' % product.pk)
        response = product_detail_view(request, product.pk)
        assert response.status_code == 200

    def test_view_product_update(self, rf):
        product = self.new_product()
        data = dict(
            title="Sample product",
            description="Sample Description",
            price=500,
            condition="N"
        )
        request = rf.post('/products/%s/update/' % product.pk, data)
        response = product_update_view(request, product.pk)
        assert response.status_code == 200

    def test_view_product_delete(self, rf):
        product = self.new_product()
        request = rf.post('/products/%s/delete/' % product.pk, {})
        response = product_delete_view(request, product.pk)
        assert response.status_code == 302
        assert response.url == "../../"

    def test_view_product_delete_not_post(self, rf):
        product = self.new_product()
        request = rf.get('/products/%s/delete/' % product.pk)
        response = product_delete_view(request, product.pk)
        assert response.status_code == 200
