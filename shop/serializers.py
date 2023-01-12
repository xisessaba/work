from rest_framework import serializers
from .models import Product, Users, Category, Sale, Brand



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'user', 'phone', 'email', 'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    # queryset = Category.objects.all()
    # seralizer_class = 
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'created_at', 'updated_at')



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price', 'image', 'description', 'lte_exists', 'created_at', 'updated_at')

class SaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id','shop', 'name', 'description', 'start_date', 'end_date', 'image', )
    


