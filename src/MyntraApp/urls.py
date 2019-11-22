from .views import *
from django.urls import path,include
from .views import *
from rest_framework import status
from rest_framework.response import Response

app_name = 'MyntraApp'

urlpatterns = [
    path('category/',api_category_list_view,name="category_list"),
    path('category/<int:id>/',api_category_id_list_view,name="category_id_list"),


    path('item/',api_item_list_view,name="item_list"),
    path('item/<int:id>/',api_item_id_list_view,name="item_id_list"),

    path('order/', api_order_list_view, name='order_list'),
    path('order/<int:id>/', api_order_id_list_view, name='order_id_list'),

    path('order/create/',api_create_order_view, name='order_create_list'),
    path('order/update/<int:id>/',api_order_details_update,name='order_update_list'),
    path('order/delete/<int:id>/',api_order_delete_list,name="order_delete"),

]
