# Generated by Django 4.1 on 2023-02-11 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_product_tb_details'),
        ('buyer', '0002_cart_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('buyerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.register_tb')),
            ],
        ),
        migrations.CreateModel(
            name='orderitem_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('totalprice', models.IntegerField()),
                ('buyerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.register_tb')),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.order_tb')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product_tb')),
            ],
        ),
    ]
