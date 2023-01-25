from prodects.models import Product, Category, Brand, Color, Masurunits, Checkout, Checkresite, User
from rest_framework import serializers

class ProductSerializtion(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
class CategorySerializtion(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializtion(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = '__all__'
        
class ColorSerializtion(serializers.ModelSerializer):
    
    class Meta:
        model = Color
        fields = '__all__'

class MasurunitsSerializtion(serializers.ModelSerializer):
    
    class Meta:
        model = Masurunits
        fields = '__all__'
        
class CheckoutSerializtion(serializers.ModelSerializer):
    
    class Meta:
        model = Checkout
        fields = '__all__'

class checkresiteSerializtion(serializers.ModelSerializer):
    
    class Meta:
        model = Checkresite
        fields = '__all__'

class UserSerializtion(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'