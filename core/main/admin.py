from django.contrib import admin
from .models import Slider, Category, Color, Size, Product, Cart
# Register your models here.

admin.site.register(Slider)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(Cart)