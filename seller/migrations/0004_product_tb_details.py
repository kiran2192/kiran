# Generated by Django 4.1 on 2023-02-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_product_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_tb',
            name='details',
            field=models.CharField(default='abc', max_length=20),
        ),
    ]
