# Generated by Django 2.2 on 2023-01-26 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_orders', '0002_auto_20230124_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='card_number',
        ),
    ]
