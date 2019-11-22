from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


@api_view(['GET',])
def api_category_list_view(request):
     name = Category.objects.all()
     if request.method == 'GET':
        serializer = CategorySerializer(name,many=True)
        return Response(serializer.data)
@api_view(['GET',])
def api_category_id_list_view(request, id):
    try:
        name = Category.objects.get(id=id)
    except Item.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            serializer = CategorySerializer(name)
            return Response(serializer.data)


@api_view(['GET',])
def api_item_list_view(request):
    item = Item.objects.all()
    if request.method == 'GET':
        serializer = ItemSerializer(item,many=True)
        return Response(serializer.data)


@api_view(['GET',])
def api_item_id_list_view(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            serializer = ItemSerializer(item)
            return Response(serializer.data)


@api_view(['GET', ])
def api_order_list_view(request):
    order = Order.objects.all()
    if request.method == 'GET':
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def api_order_id_list_view(request, id):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            serializer = OrderSerializer(order)
            return Response(serializer.data)


@api_view(['POST', ])
def api_create_order_view(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['Success'] = 'Order Created Successfully'
            return Response(data=data)
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def api_order_details_update(request, id):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Update/Put operation successful'
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['DELETE', ])
def api_order_delete_list(request, id):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        data = {}
        operation = order.delete()
        if operation:
            data['Success'] = 'Order Deleted successfully'
        else:
            data["Failure"] = "Delete Failed"
        return Response(data=data, status=status.HTTP_200_OK)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

