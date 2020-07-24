from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
from rest_framework.authtoken.models import Token

from api.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['barcode', 'product_description', 'product_name', 'product_brand', 'product_score']

    def create(self, validated_data):
        return Products.objects.create(**validated_data)