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
]