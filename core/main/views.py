from django.shortcuts import render
from .models import Slider, Category

# Create your views here.

def index(request):
    slider_active = Slider.objects.first()
    slider = Slider.objects.all()[1:]
    category_list = Category.objects.all()
    return render(request, 'index.html', context={
        'nav_item':'index' ,
        'slider_active':slider_active,
        'slider':slider,
        'category_list':category_list
    })

def cart(request):
    category_list = Category.objects.all()
    return render(request, 'cart.html', context={
        'nav_item':'cart' ,
        'category_list':category_list

        
    })


def checkout(request):
    category_list = Category.objects.all()
    return render(request, 'checkout.html', context={
        'nav_item':'checkout',
        'category_list':category_list

        
    })


def contact(request):
    category_list = Category.objects.all()

    return render(request, 'contact.html', context={
        'nav_item':'contact',
        'category_list':category_list

        
    })


def detail(request):
    category_list = Category.objects.all()

    return render(request, 'detail.html', context={
        'nav_item': 'detail',
        'category_list':category_list

        
    })


def shop(request):
    category_list = Category.objects.all()

    return render(request, 'shop.html', context={
        'nav_item': 'shop',
        'category_list':category_list

        
    })