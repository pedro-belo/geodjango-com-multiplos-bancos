from django.contrib import admin

from core import models


@admin.register(models.Cities)
class CitiesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Seller)
class SellerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    pass
