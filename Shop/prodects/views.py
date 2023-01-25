from django.shortcuts import render
from .models import Product, Category, Brand, Color, Masurunits, Checkout, Checkresite, User
from rest_framework import viewsets, permissions
from .serializers import UserSerializtion, ProductSerializtion, CategorySerializtion, BrandSerializtion, ColorSerializtion, MasurunitsSerializtion, CheckoutSerializtion, checkresiteSerializtion
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializtion
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializtion
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializtion

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializtion
    
class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializtion

class MasurunitsViewSet(viewsets.ModelViewSet):
    queryset = Masurunits.objects.all()
    serializer_class = MasurunitsSerializtion
    
class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializtion
    
class CheckresiteViewSet(viewsets.ModelViewSet):
    queryset = Checkresite.objects.all()
    serializer_class = checkresiteSerializtion

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializtion