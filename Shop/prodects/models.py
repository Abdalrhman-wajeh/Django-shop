from django.db import models

# Create your models here.


class Product(models.Model):

    USD = 'USD'
    IQD = 'IQD'
    currency = [
        (USD, '$'),
        (IQD, 'دينار'),
    ]
    S = 'S'
    M = 'M'
    L = 'L'
    XL = 'XL'
    _2XL = '2XL'
    _3XL = '3XL'
    _4XL = '4XL'
    _5XL = '5XL'
    Sizes = [
        (S, 'S'), (M, 'M'), (L, 'L'), (XL, 'XL'), (_2XL,
                                                   '2XL'), (_3XL, '3XL'), (_4XL, '4XL'), (_5XL, '5XL')
    ]

    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    price_currency = models.CharField(
        max_length=120, choices=currency, default="USD")
    quantety = models.IntegerField(default=1)
    packigedimantions = models.CharField(
        "Demantions", max_length=120, blank=True, null=True)
    size = models.CharField("Clothes Size", max_length=120,
                            choices=Sizes, blank=True, null=True)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE,blank=True, null=True)
    Brand = models.ForeignKey('Brand', on_delete=models.CASCADE,blank=True, null=True)
    Color = models.ForeignKey(
        'Color', on_delete=models.CASCADE, blank=True, null=True)
    Masur_units = models.ForeignKey(
        'Masurunits', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='product_image', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    editdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Masurunits(models.Model):
    name = models.CharField("Unit name", max_length=120, default="none")
    date = models.DateTimeField(auto_now_add=True)
    editdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField("Color name", max_length=120, default="none")
    date = models.DateTimeField(auto_now_add=True)
    editdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("Catagpry name", max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    editdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField("Brand name", max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    editdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Checkout(models.Model):
    
    zain_cash = 'Zcash'
    on_delivery = 'OnD'
    payments = [(zain_cash, 'Zain Cash'), (on_delivery, 'On Delivery')]

    name = models.CharField("Name", max_length=120)
    email = models.EmailField("Email", max_length=120)
    address = models.CharField("Address", max_length=120)
    city = models.CharField("City", max_length=120)
    paymentmethod = models.CharField(
        "Payment Method", max_length=120, choices=payments)
    total = models.DecimalField("Total", decimal_places=2, max_digits=10000)
    date = models.DateTimeField(auto_now_add=True)
    editdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Checkresite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    quantety = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    editdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (self.product.name, self.checkout.email)


class User(models.Model):
    name = models.CharField("Name", max_length=120)
    email = models.EmailField("Email", max_length=120)
    password = models.CharField("Password", max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    editdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
