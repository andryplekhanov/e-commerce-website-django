# Generated by Django 2.2 on 2023-01-19 09:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_product', '0002_auto_20230118_1209'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_type', models.CharField(choices=[('1', 'Обычная доставка'), ('2', 'Экспресс доставка')], default='1', max_length=30, verbose_name='способ доставки')),
                ('delivery_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='стоимость доставки')),
                ('payment_type', models.CharField(choices=[('1', 'Онлайн картой'), ('2', 'Онлайн со случайного чужого счета')], default='1', max_length=30, verbose_name='способ оплаты')),
                ('address', models.CharField(max_length=255, verbose_name='адрес получателя')),
                ('city', models.CharField(max_length=100, verbose_name='город')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('paid', models.BooleanField(default=False, verbose_name='оплачен')),
                ('card_number', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)], verbose_name='номер карты')),
                ('status', models.CharField(blank=True, max_length=150, null=True, verbose_name='статус платежа')),
                ('payment_code', models.IntegerField(default=0, verbose_name='код оплаты')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app_orders.Order', verbose_name='заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='app_product.Product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
    ]