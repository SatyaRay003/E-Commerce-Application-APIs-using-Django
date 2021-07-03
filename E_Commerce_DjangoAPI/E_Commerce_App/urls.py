from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^customer_order/$', views.customer_order_api),
    url(r'^customer_order/([\w+]+)$', views.customer_order_api),

    url(r'^inventory_management/$', views.Inventory_management_api),
    url(r'^inventory_management/([\w+]+)$', views.Inventory_management_api),

    url(r'^purchase_order/$', views.Purchase_Order_api),
    url(r'^purchase_order/([\w+]+)$', views.Purchase_Order_api)

]
