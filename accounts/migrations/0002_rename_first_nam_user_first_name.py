# Generated by Django 5.0.7 on 2024-07-22 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_nam',
            new_name='first_name',
        ),
    ]