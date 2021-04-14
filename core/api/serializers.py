from core import models
from django.db.models import Count, Sum
from geo_app import facade
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    offers = serializers.SerializerMethodField()

    unit = serializers.SerializerMethodField()

    def get_unit(self, product):
        return product.get_unit_display()

    def get_offers(self, product):

        queryset = product.marketplace\
            .values('seller__city', 'seller__city__name', 'seller__city__ibge_id')\
            .annotate(
                total_offers=Count('seller__city'),
                total_quantity=Sum('quantity'))

        municipios = []
        for item in queryset:
            municipios.append({
                'mid': item['seller__city'],
                'name': item['seller__city__name'],
                'total_offers': item['total_offers'],
                'total_quantity': item['total_quantity'],
                'coords': facade.get_coords(item['seller__city__ibge_id'])
            })

        return municipios

    class Meta:
        model = models.Product
        fields = ('name', 'unit', 'offers')
