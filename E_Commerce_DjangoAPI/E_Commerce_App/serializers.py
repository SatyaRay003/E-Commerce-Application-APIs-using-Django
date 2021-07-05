from django.db.models import fields
from rest_framework import serializers

from .models import  Customer_Order, Inventory_management, Purchase_Order


class Customer_Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Order
        fields = ('Item_Name', 'Order_Id', 'Customer_Name', 
                  'Customer_Address', 'Quantity', 'Price', 'Payment_status', 'Order_Date')

class Inventory_management_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory_management
        fields = ('Item_Name', 'Item_Id', 'Quantity')

class Purchase_Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_Order
        fields = ('Item_Name', 'Item_Id', 'Supplier_Name', 
                  'Quantity', 'Creation_Date_time', 'Last_Modified_Date_time')
