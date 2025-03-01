from django.db import models
from catalogs.models import Catalog


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
