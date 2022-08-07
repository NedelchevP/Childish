from rest_framework import serializers
from onlinestore.models import Product, Orders


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'date', 'products']


class ApiStatsSerializer(serializers.Serializer):
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    metric = serializers.ChoiceField(choices=['price', 'count'])

