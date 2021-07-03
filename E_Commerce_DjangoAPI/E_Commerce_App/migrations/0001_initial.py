# Generated by Django 3.2.4 on 2021-07-02 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Order',
            fields=[
                ('Date_time', models.DateTimeField(auto_created=True)),
                ('Item_Name', models.CharField(max_length=50)),
                ('Item_Id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Customer_Name', models.CharField(max_length=50)),
                ('Customer_Address', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('Price', models.FloatField()),
                ('Payment_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventory_management',
            fields=[
                ('Item_Name', models.CharField(max_length=50)),
                ('Item_Id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Order',
            fields=[
                ('Date_time', models.DateTimeField(auto_created=True)),
                ('Item_Name', models.CharField(max_length=50)),
                ('Item_Id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Suuplier_Name', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
            ],
        ),
    ]