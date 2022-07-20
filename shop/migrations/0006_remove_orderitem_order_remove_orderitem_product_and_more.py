# Generated by Django 4.0.5 on 2022-07-18 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='unit_price',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='membership',
        ),
        migrations.RemoveField(
            model_name='product',
            name='last_update',
        ),
        migrations.RemoveField(
            model_name='product',
            name='promotions',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Promotion',
        ),
    ]
