from django.urls import path
from products.views import create_product, product_list

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/create/', create_product, name='create-product'),
]
