from django.shortcuts import render, redirect
from .models import Slider, Category, Product, Cart
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
# import logging
from django.views.decorators.csrf import csrf_exempt



# logging.basicConfig(level=logging.INFO)



def get_items_count_in_cart():
    count_sum = 0
    price_sum = 0
    for i in Cart.objects.all():
        count_sum += i.count
        price_sum += i.total_price
    return [count_sum, price_sum]


def index(request):
    slider_active = Slider.objects.first()
    slider = Slider.objects.all()[1:]
    category_list = Category.objects.all()
    cart_list_count = get_items_count_in_cart()[0]

    return render(request, 'index.html', context={
        'nav_item':'index' ,
        'slider_active':slider_active,
        'slider':slider,
        'category_list':category_list,
        'cart_list_count':cart_list_count

    })

def cart(request):
    category_list = Category.objects.all()
    cart_list_count = get_items_count_in_cart()[0]
    cart_list_price_sum = get_items_count_in_cart()[1]
    cart_list = Cart.objects.all()
    shipping_price = round(cart_list_price_sum * 10 / 100)
    return render(request, 'cart.html', context={
        'nav_item':'cart' ,
        'category_list':category_list,
        'cart_list':cart_list,
        'cart_list_count':cart_list_count,
        'cart_list_price_sum':cart_list_price_sum,
        'shipping_price':shipping_price,
        'full_price':cart_list_price_sum + shipping_price

    })


def checkout(request):
    category_list = Category.objects.all()
    cart_list_count = get_items_count_in_cart()[0]

    return render(request, 'checkout.html', context={
        'nav_item':'checkout',
        'category_list':category_list,
        'cart_list_count':cart_list_count


        
    })


def shop(request):
    category_list = Category.objects.all()
    product_list = Product.objects.all()
    cart_list_count = get_items_count_in_cart()[0]
    

    # Paginate the products: 6 products per page
    paginator = Paginator(product_list, 6)
    page_number = request.GET.get('page')  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)  # Get the products for the current page

    return render(request, 'shop.html', context={
        'nav_item': 'shop',
        'category_list': category_list,
        'product_list': page_obj,  # Pass paginated products
        'cart_list_count':cart_list_count
        
        
    })

def shop_filter(request, id):
    category_list = Category.objects.all()
    product_list = Product.objects.filter(category_id=id)
    cart_list_count = get_items_count_in_cart()[0]

    return render(request, 'shop.html', context={
        'category_list': category_list,
        'product_list': product_list,  # Pass paginated products
        'cart_list_count':cart_list_count



    })


def detail(request, id):
    category_list = Category.objects.all()
    product = Product.objects.get(pk=id)
    cart_list_count = get_items_count_in_cart()[0]

    return render(request, 'detail.html', context={
        'nav_item': 'detail',
        'category_list':category_list,
        'product':product,
        'cart_list_count':cart_list_count


        
    })


def contact(request):
    category_list = Category.objects.all()
    cart_list_count = get_items_count_in_cart()[0]


    return render(request, 'contact.html', context={
        'nav_item':'contact',
        'category_list':category_list,
        'cart_list_count':cart_list_count

    })


def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        prod = Product.objects.get(id=product_id)
        for i in Cart.objects.all():
            if prod == i.product:
                prod_cart = Cart.objects.get(product=prod)
                prod_cart.count += 1
                prod_cart.total_price = (prod.discount_price * prod_cart.count)
                prod_cart.save()
                break
        else:
            Cart.objects.create(product=prod, count=1, total_price = prod.discount_price)
        return redirect('shop')
    
    
def delete_from_cart(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        Cart.objects.filter(id=cart_id).delete()
        return redirect('cart')

@csrf_exempt
def add_product_count(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        cart_object = Cart.objects.get(id=cart_id)
        cart_object.count += 1
        cart_object.total_price = cart_object.product.discount_price * cart_object.count
        cart_object.save()
        return redirect('cart')

@csrf_exempt
def subtract_product_count(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        cart_object = Cart.objects.get(id=cart_id)
        cart_object.count -= 1
        cart_object.total_price = cart_object.product.discount_price * cart_object.count
        cart_object.save()
        return redirect('cart')
