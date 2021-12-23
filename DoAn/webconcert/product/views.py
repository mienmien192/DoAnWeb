from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import *
from django.conf import settings
from django.http import JsonResponse
import json
# Create your views here.
User = settings.AUTH_USER_MODEL
def pro(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    product = Product.objects.all()
    context = {'product': product, 'cartItems':cartItems}
    return render(request, 'product/product.html', context)

def show(request):
    product = Product.objects.all()
    return render(request,'show.html',{'product':product})

def emp(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ProductForm()
    return render(request,'index.html',{'form':form})

def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request,'edit.html', {'product':product})
def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance = product)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'product':product})
def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/show")

# Create your views here.
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(title__contains = searched)
        return render(request, 'search.html',{'searched':searched}, )

    else:

        return render(request, 'search.html',)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'product/cart.html', context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order, 'cartItems':cartItems}
    return render(request, 'product/checkout.html', context)



def updateItem(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    print('action: ', action)
    print('product_id: ', product_id)

    customer = request.user.customer
    product = Product.objects.get(id=product_id)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added.', safe=False)

def processOrder(request):
    print('Data:', request.body)
    return JsonResponse('Payment complete!.', safe=False)
