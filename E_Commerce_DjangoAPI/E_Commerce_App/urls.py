from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^customer_order/$', views.customer_order_api),
    url(r'^customer_order/([\w+]+)$', views.customer_order_api)

]