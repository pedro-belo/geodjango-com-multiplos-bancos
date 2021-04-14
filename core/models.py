from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class Cities(models.Model):
    state = models.CharField(max_length=2)
    name = models.CharField(max_length=255)
    ibge_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'
        db_table = 'cities'


class Seller(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='seller')
    city = models.ForeignKey('Cities', on_delete=models.CASCADE, related_name='seller')

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
        db_table = 'seller'


class Product(models.Model):

    class Units(models.IntegerChoices):
        KILOGRAM = 1, _('KG')
        LITRO = 2, _('L')
        UNIDADE = 3, _('UND')

    name = models.CharField(max_length=50, unique=True)
    unit = models.PositiveSmallIntegerField(choices=Units.choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        db_table = 'product'


class Marketplace(models.Model):

    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='marketplace')

    seller = models.ForeignKey(
        'Seller', on_delete=models.PROTECT, related_name='marketplace')

    quantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Mercado'
        verbose_name_plural = 'Mercados'
        db_table = 'marketplace'

        constraints = [
            models.UniqueConstraint(fields=['seller', 'product'], name='unique_seller_product')
        ]
