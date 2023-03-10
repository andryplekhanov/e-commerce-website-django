# Generated by Django 2.2 on 2023-01-28 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_product', '0001_initial'),
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
                ('status', models.CharField(blank=True, max_length=150, null=True, verbose_name='статус')),
                ('payment_code', models.IntegerField(default=0, verbose_name='код оплаты')),
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
