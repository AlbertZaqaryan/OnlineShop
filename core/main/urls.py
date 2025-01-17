from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('shop/', views.shop, name='shop'),
    path('shop_filter/<int:id>', views.shop_filter, name='shop_filter'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/', views.delete_from_cart, name='delete_from_cart'),
    path('add_product_count/', views.add_product_count, name='add_product_count'),
    path('subtract_product_count/', views.subtract_product_count, name='subtract_product_count'),
]