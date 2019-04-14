from django.db import models
from django.urls import reverse


# Create your models here.
class ProductCondition(models.Model):
    code = models.CharField(max_length=1, null=False, blank=False, primary_key=True)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.description


class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False)  # null=True, default=True
    condition = models.ForeignKey(ProductCondition, default="N", on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})  # f"/products/{self.id}/"
