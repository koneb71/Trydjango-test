import pytest
from django.db import IntegrityError

from products.models import Product, ProductCondition


pytestmark = pytest.mark.django_db


class TestProductModel:

    def test_save(self):
        product = Product.objects.create(
            title="Sample product",
            description="Sample Description",
            summary="Sample Description",
            price=500,
            featured=True
        )
        assert product.title == "Sample product"
        assert product.price == 500
        assert product.description == "Sample Description"
        assert product.featured == True
        assert product.get_absolute_url() == "/products/%s/" % product.pk

    def test_no_price(self):
        with pytest.raises(IntegrityError):
            Product.objects.create(title="Sample")



class TestProductConditionModel:

    def test_save(self):
        condition = ProductCondition.objects.create(
            code='N',
            description="New"
        )
        assert condition.code == "N"
        assert condition.description == "New"
        assert str(condition) == "New"