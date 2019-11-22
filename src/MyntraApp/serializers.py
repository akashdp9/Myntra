from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CatergoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','get_image',)

class ItemSerializer(serializers.ModelSerializer):
    category_name = CatergoryNameSerializer()
    image_url = serializers.CharField(source='get_image')
    class Meta:
        model = Item
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'