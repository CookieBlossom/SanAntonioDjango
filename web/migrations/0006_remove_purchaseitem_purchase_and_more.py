# Generated by Django 5.0.6 on 2024-06-30 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_size_size_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseitem',
            name='purchase',
        ),
        migrations.RemoveField(
            model_name='purchaseitem',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='purchaseitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
        migrations.DeleteModel(
            name='PurchaseItem',
        ),
    ]
