from rest_framework import routers
from django.urls import include, path
from prodects import views



routers = routers.DefaultRouter()
routers.register('users', views.UserViewSet)
routers.register('products', views.ProductViewSet)
routers.register('category', views.CategoryViewSet)
routers.register('brand', views.BrandViewSet)
routers.register('color', views.ColorViewSet)
routers.register('masurunits', views.MasurunitsViewSet)
routers.register('checkout', views.CheckoutViewSet)
routers.register('checkresite', views.CheckresiteViewSet)
routers.register('users', views.UserViewSet)


urlpatterns = [
    path('', include(routers.urls)),
]
