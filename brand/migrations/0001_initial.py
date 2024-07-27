# Generated by Django 5.0.7 on 2024-07-27 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=30)),
                ('brand_image', models.ImageField(upload_to='brand_image/')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]