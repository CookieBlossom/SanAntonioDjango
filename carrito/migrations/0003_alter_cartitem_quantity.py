# Generated by Django 5.0.6 on 2024-07-02 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_cartitem_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
