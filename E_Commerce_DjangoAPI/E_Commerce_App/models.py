from django.db import models

# Create your models here.


class Customer_Order(models.Model):

    Item_Name = models.CharField(max_length=50, null=False)
    Order_Id = models.CharField(max_length=50, primary_key=True)
    Customer_Name = models.CharField(max_length=50, null=False)
    Customer_Address = models.CharField(max_length=50, null=False)
    Quantity = models.IntegerField(null=False)
    Price = models.FloatField(null=False)
    # Payment_status = models.BooleanField(null=False)
    # Date_time = models.DateTimeField(auto_created=True)
    

    def __str__(self):
        return "Customer: %s" %self.Customer_Name

    @property
    def Serial_Id(self): return self.id

class Inventory_management(models.Model):

    Item_Name = models.CharField(max_length=50, null=False)
    Item_Id = models.CharField(max_length=50, primary_key=True)
    Quantity = models.IntegerField(null=False)

    def __str__(self):
        return "Item: %s"%self.Item_Name

    @property
    def Serial_Id(self): return self.id

class Purchase_Order(models.Model):

    Item_Name = models.CharField(max_length=50, null=False)
    Item_Id = models.CharField(max_length=50, primary_key=True)
    Suuplier_Name = models.CharField(max_length=50, null=False)
    Quantity = models.IntegerField(null=False)
    Date_time = models.DateTimeField(auto_created=True)


    def __str__(self):
        return "Item: %s from %s"% (self.Item_Name, self.Suuplier_Name)

    @property
    def Serial_Id(self): return self.id

