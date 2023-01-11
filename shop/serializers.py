from rest_framework import serializers
from .models import Product, Users, Category, Sale



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'user', 'phone', 'email', 'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price', 'image', 'description', 'lte_exists', 'created_at', 'updated_at')

class SaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'user', 'product', 'quantity', 'total_price', 'created_at', 'updated_at')

