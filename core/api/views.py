from rest_framework import generics
from core.models import Product
from core.api import serializers
from rest_framework import permissions


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.AllowAny,)
