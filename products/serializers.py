from rest_framework import serializers
from .models import Products, Category, ProductPictures


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['logo', 'name', 'identifier']
        read_only_fields = ['identifier']


class ProductPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPictures
        fields = ['pictures']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)

    class Meta:
        model = Products
        fields = [
            'name',
            'description',
            'category',
            'status',
            'base_price',
            'identifier',
            'is_editable',
            'created_at'
        ]
        read_only_fields = ['status', 'identifier']
