from rest_framework import serializers
from .models import Product,  Category, Sale, Brand, ProductColor, Applications





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id','category', 'name',  'created_at', 'updated_at')


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ('id', 'name', 'created_at', 'updated_at')
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price', 'image', 'description', 'lte_exists', 'created_at', 'updated_at')

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id','shop', 'name', 'description', 'start_date', 'end_date', 'image', )
    

class ApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applications
        fields = ('id', 'shop', 'name', 'phone', 'whatsapp', 'message', 'created_at', 'updated_at', )
        

