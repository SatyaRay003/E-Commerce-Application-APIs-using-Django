# Generated by Django 3.2.4 on 2021-07-03 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerce_App', '0002_rename_item_id_customer_order_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_order',
            name='Date_time',
        ),
        migrations.RemoveField(
            model_name='customer_order',
            name='Payment_status',
        ),
    ]
