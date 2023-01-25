from django.contrib import admin
from .models import Product, Category, Brand, Color, Masurunits, Checkout, Checkresite
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Masurunits)
admin.site.register(Checkout)
admin.site.register(Checkresite)