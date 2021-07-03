from re import I, S
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Customer_Order, Inventory_management, Purchase_Order
from .serializers import Customer_Order_Serializer, Inventory_management_Serializer, Purchase_Order_Serializer

from rest_framework.exceptions import ParseError

import json


# Create your views here.

def field_error_handler(data, columns):

    data = dict(data)
    key = data.keys()
    message = 'Please Provide: '

    for i in columns:

        if (i not in key) or (str(data[i]).strip()==''):
            message += i + '  '

    if message == 'Please Provide: ':
        return False, 0
    return True, JsonResponse(message, safe=False)

ParseError_massege = '''You have done any of these four possible errors: You\'ve forgot to put value / Value is not provided with double quotes / Comma is missing / Extra Comma is given'''


#################################################################################################
#######                          CUSTOMER ORDER API                                       #######                             
#################################################################################################


@csrf_exempt
def customer_order_api(request, id=0):

    columns = ('Item_Name', 'Order_Id', 'Customer_Name', 
                  'Customer_Address', 'Quantity', 'Price')
    
    print(id, type(id))

    # GET Method
    if request.method == 'GET':

        # return all the entries from the database
        if id == 0:
            items = Customer_Order.objects.all()
            items_ser = Customer_Order_Serializer(items, many=True)
            if list(items_ser.data) == []:
                return JsonResponse('Database is empty, PLease add data', safe=False)
            return JsonResponse(items_ser.data, safe=False)

        # return a single entry by the existed Primary Key,Order_Id from the database 
        elif id != 0:
            try:
                item = Customer_Order.objects.get(Order_Id=id)
                item_ser = Customer_Order_Serializer(item)
                return JsonResponse(item_ser.data, safe=False)
            except Customer_Order.DoesNotExist:
                return JsonResponse('This Order Id doesn\'t exist, PLease provide valid Order Id', safe=False)

    # POST Method
    elif request.method == 'POST':

        try:
            item = JSONParser().parse(request)

            chcek = field_error_handler(item, columns)

            if chcek[0]:
                return chcek[1]

            try:
                order = Customer_Order.objects.get(Order_Id=item['Order_Id'])
                return JsonResponse('This Order Id already exist, Please use new Order Id to add the data', safe=False)

            except Customer_Order.DoesNotExist:
                item_ser = Customer_Order_Serializer(data=item)

                if item_ser.is_valid():
                    item_ser.save()
                    return JsonResponse('Order is added Successfully!!', safe=False)

                return JsonResponse('Failed to add the Order', safe=False)

        except ParseError:
            return JsonResponse(ParseError_massege, safe=False)

    # PUT Method
    elif request.method == 'PUT':

        try:
            item_data = JSONParser().parse(request)

            try:
                order = Customer_Order.objects.get(Order_Id=item_data['Order_Id'])

                order_ser = Customer_Order_Serializer(order)
                order_ser_json = JsonResponse(order_ser.data, safe=False)
                order_content = order_ser_json.content
                order_dict = json.loads(order_content.decode('utf-8'))

                if order_dict == item_data:
                    return JsonResponse('No changes Found!, Please provide new data to update', safe=False)

                else:
                    item_data_ser = Customer_Order_Serializer(order ,data=item_data)

                    if item_data_ser.is_valid():
                        item_data_ser.save()
                        return JsonResponse('Order is Updated Successfully!!', safe=False)

                    return JsonResponse('Failed to Update the order, Please Provide the value along with Column Name', safe=False)

                
            except KeyError:
                return JsonResponse('Please provide the Order Id to update the data', safe=False)

            except Customer_Order.DoesNotExist:
                return JsonResponse('The item doesn\'t exist, Please Provide valid Order Id to Update', safe=False)   

        except ParseError:
            return JsonResponse(ParseError_massege, safe=False)
            

    # Delete Method
    elif request.method == 'DELETE':

        try:
            item = Customer_Order.objects.get(Order_Id=id)
            item.delete()
            return JsonResponse('Deleted Successfully!!', safe=False)   

        except Customer_Order.DoesNotExist:
            return JsonResponse('The item doesn\'t exist, Please Provide valid Order Id to delete', safe=False)


#################################################################################################
#######                          INVENTORY MANAGEMENT API                                 #######                             
#################################################################################################

        
@csrf_exempt
def Inventory_management_api(request, id=0):
    
    columns = ('Item_Name', 'Item_Id', 'Quantity')

    # GET Method
    if request.method == 'GET':

        # return all the entries from the database
        if id == 0:
            items = Inventory_management.objects.all()
            items_ser = Inventory_management_Serializer(items, many=True)
            if list(items_ser.data) == []:
                return JsonResponse('Database is empty, PLease add data', safe=False)
            return JsonResponse(items_ser.data, safe=False)

        # return a single entry by the existed Primary Key,Order_Id from the database 
        elif id != 0:
            try:
                item = Inventory_management.objects.get(Item_Id=id)
                item_ser = Inventory_management_Serializer(item)
                return JsonResponse(item_ser.data, safe=False)
            except Inventory_management.DoesNotExist:
                return JsonResponse('This Item Id doesn\'t exist, PLease provide valid Order Id', safe=False)

    # POST Method
    elif request.method == 'POST':

        try:
            item = JSONParser().parse(request)

            check = field_error_handler(item, columns)

            if check[0]:
                return check[1]

            try:
                order = Inventory_management.objects.get(Item_Id=item['Item_Id'])
                return JsonResponse('This Item Id already exist, Please use new Item Id to add the data', safe=False)

            except Inventory_management.DoesNotExist:
                item_ser = Inventory_management_Serializer(data=item)

                if item_ser.is_valid():
                    item_ser.save()
                    return JsonResponse('Item is added Successfully!!', safe=False)

                return JsonResponse('Failed to add the Item', safe=False)

        except ParseError:
            return JsonResponse(ParseError_massege, safe=False)

    # PUT Method
    elif request.method == 'PUT':

        try:
            item_data = JSONParser().parse(request)

            try:
                order = Inventory_management.objects.get(Item_Id=item_data['Item_Id'])

                order_ser = Inventory_management_Serializer(order)
                order_ser_json = JsonResponse(order_ser.data, safe=False)
                order_content = order_ser_json.content
                order_dict = json.loads(order_content.decode('utf-8'))

                if order_dict == item_data:
                    return JsonResponse('No changes Found!, Please provide new data to update', safe=False)

                else:
                    item_data_ser = Inventory_management_Serializer(order ,data=item_data)

                    if item_data_ser.is_valid():
                        item_data_ser.save()
                        return JsonResponse('Item is Updated Successfully!!', safe=False)

                    return JsonResponse('Failed to Update the Item, Please Provide the value along with Column Name', safe=False)

                
            except KeyError:
                return JsonResponse('Please provide the Item Id to update the data', safe=False)

            except Inventory_management.DoesNotExist:
                return JsonResponse('The item doesn\'t exist, Please Provide valid Item Id to Update', safe=False)   

        except ParseError:
            return JsonResponse(ParseError_massege, safe=False)
            

    # Delete Method
    elif request.method == 'DELETE':

        try:
            item = Inventory_management.objects.get(Item_Id=id)
            item.delete()
            return JsonResponse('Deleted Successfully!!', safe=False)   

        except Inventory_management.DoesNotExist:
            return JsonResponse('The item doesn\'t exist, Please Provide valid Item Id to delete', safe=False)


#################################################################################################
#######                          PURCHASE ORDER API                                       #######                             
#################################################################################################


@csrf_exempt
def Purchase_Order_api(request, id=0):
    
    columns = ('Item_Name', 'Item_Id', 'Supplier_Name', 
                  'Quantity')

    # GET Method
    if request.method == 'GET':

        # return all the entries from the database
        if id == 0:
            items = Purchase_Order.objects.all()
            items_ser = Purchase_Order_Serializer(items, many=True)
            if list(items_ser.data) == []:
                return JsonResponse('Database is empty, PLease add data', safe=False)
            return JsonResponse(items_ser.data, safe=False)

        # return a single entry by the existed Primary Key,Order_Id from the database 
        elif id != 0:
            try:
                item = Purchase_Order.objects.get(Item_Id=id)
                item_ser = Purchase_Order_Serializer(item)
                return JsonResponse(item_ser.data, safe=False)
            except Purchase_Order.DoesNotExist:
                return JsonResponse('This Item Id doesn\'t exist, PLease provide valid Order Id', safe=False)

    # POST Method
    elif request.method == 'POST':

        try:
            item = JSONParser().parse(request)

            check = field_error_handler(item, columns)

            if check[0]:
                return check[1]

            try:
                order = Purchase_Order.objects.get(Item_Id=item['Item_Id'])
                return JsonResponse('This Item Id already exist, Please use new Item Id to add the data', safe=False)

            except Purchase_Order.DoesNotExist:
                item_ser = Purchase_Order_Serializer(data=item)

                if item_ser.is_valid():
                    item_ser.save()
                    return JsonResponse('Item is added Successfully!!', safe=False)

                return JsonResponse('Failed to add the Item', safe=False)

        except ParseError:
            return JsonResponse(ParseError_massege, safe=False)

    # PUT Method
    elif request.method == 'PUT':

        try:
            item_data = JSONParser().parse(request)

            try:
                order = Purchase_Order.objects.get(Item_Id=item_data['Item_Id'])

                order_ser = Purchase_Order_Serializer(order)
                order_ser_json = JsonResponse(order_ser.data, safe=False)
                order_content = order_ser_json.content
                order_dict = json.loads(order_content.decode('utf-8'))



                if list(order_dict.items())[:4] == list(item_data.items()):
                    return JsonResponse('No changes Found!, Please provide new data to update', safe=False)

                else:
                    item_data_ser = Purchase_Order_Serializer(order ,data=item_data)

                    if item_data_ser.is_valid():
                        item_data_ser.save()
                        return JsonResponse('Item is Updated Successfully!!', safe=False)

                    return JsonResponse('Failed to Update the Item, Please Provide the value along with Column Name', safe=False)

                
            except KeyError:
                return JsonResponse('Please provide the Item Id to update the data', safe=False)

            except Purchase_Order.DoesNotExist:
                return JsonResponse('The item doesn\'t exist, Please Provide valid Item Id to Update', safe=False)   

        except ParseError:
            return JsonResponse(ParseError_massege, safe=False)
            

    # Delete Method
    elif request.method == 'DELETE':

        try:
            item = Purchase_Order.objects.get(Item_Id=id)
            item.delete()
            return JsonResponse('Deleted Successfully!!', safe=False)   

        except Purchase_Order.DoesNotExist:
            return JsonResponse('The item doesn\'t exist, Please Provide valid Item Id to delete', safe=False)

