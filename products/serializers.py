from rest_framework import serializers
from .models import Product
from catalogs.models import Catalog
from catalogs.serializers import CatalogSerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CatalogSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Catalog.objects.all(), write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'category_id']
