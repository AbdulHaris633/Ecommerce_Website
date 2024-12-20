from rest_framework import serializers

from catalogue.models import Category, Product, ProductClass


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = "__all__"


class ProductClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductClass
        fields = "__all__"
