from rest_framework  import serializers
from products.serializers import ProductSerializer
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'customer_email', 'customer_phone', 'items', 'total_price', 'status',
                  'shipping_address', 'created_at']