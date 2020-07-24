import json

from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from api.Serializers.productSerializer import ProductsSerializer

from rest_framework.permissions import IsAuthenticated

from api.models import Products


class ProductView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductSearch(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        products = Products.objects.filter(barcode=request.data.get('barcode'))
        if products:
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response('No entry', status=status.HTTP_204_NO_CONTENT)
