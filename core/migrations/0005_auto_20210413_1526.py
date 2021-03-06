# Generated by Django 3.2 on 2021-04-13 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_seller_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='ibge_id',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='marketplace',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='marketplace', to='core.seller'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.PositiveSmallIntegerField(choices=[(1, 'KG'), (2, 'L'), (3, 'UND')]),
        ),
        migrations.AddConstraint(
            model_name='marketplace',
            constraint=models.UniqueConstraint(fields=('seller', 'product'), name='unique_seller_product'),
        ),
    ]
