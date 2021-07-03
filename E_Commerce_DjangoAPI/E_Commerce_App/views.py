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

def field_error_handler(data):

    data = dict(data)
    key = data.keys()
    message = 'Please Provide: '

    columns = ('Item_Name', 'Order_Id', 'Customer_Name', 
                  'Customer_Address', 'Quantity', 'Price')

    for i in columns:

        if (i not in key) or (str(data[i]).strip()==''):
            message += i + '  '

    if message == 'Please Provide: ':
        return False, 0
    return True, JsonResponse(message, safe=False)

ParseError_massege = '''You have done any of these four possible errors: You\'ve forgot to put value / Value is not provided with double quotes / Comma is missing / Extra Comma is given'''


@csrf_exempt
def customer_order_api(request, id=0):
    
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

            if field_error_handler(item)[0]:
                return field_error_handler(item)[1]

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




        




