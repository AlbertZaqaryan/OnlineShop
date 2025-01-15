from django.shortcuts import render
from .models import Slider, Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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


def shop(request):
    category_list = Category.objects.all()
    product_list = Product.objects.all()

    # Paginate the products: 6 products per page
    paginator = Paginator(product_list, 6)
    page_number = request.GET.get('page')  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)  # Get the products for the current page

    return render(request, 'shop.html', context={
        'nav_item': 'shop',
        'category_list': category_list,
        'product_list': page_obj,  # Pass paginated products
    })

def shop_filter(request, id):
    category_list = Category.objects.all()
    product_list = Product.objects.filter(category_id=id)

    return render(request, 'shop.html', context={
        'category_list': category_list,
        'product_list': product_list,  # Pass paginated products

    })


def detail(request, id):
    category_list = Category.objects.all()
    product = Product.objects.get(pk=id)
    return render(request, 'detail.html', context={
        'nav_item': 'detail',
        'category_list':category_list,
        'product':product
        
    })
