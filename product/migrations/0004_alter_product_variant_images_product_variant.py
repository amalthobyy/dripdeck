# Generated by Django 5.0.7 on 2024-08-05 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_variant_images_product_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_variant_images',
            name='product_variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product_variant'),
        ),
    ]
