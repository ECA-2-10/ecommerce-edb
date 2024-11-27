import json

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render

from product.models import Product


def add_to_cart(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('cart:view_cart')
    
    if product.stock == 0:
        return redirect('cart:view_cart')
    else:
        cart = request.COOKIES.get('cart')
        cart = json.loads(cart) if cart else {}

        if product.stock - cart[str(product_id)]['quantity'] - 1 < 0:
            return redirect('cart:view_cart')

        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] += 1
            cart[str(product_id)]['total'] = round(cart[str(product_id)]['price'] * cart[str(product_id)]['quantity'], 2)
        else:
            cart[str(product_id)] = {
                "id": product_id,
                "name": product.name,
                "price": float(product.price),
                "quantity": 1,
                "total": float(product.price),
                "image": product.image.url
            }

        response = redirect('cart:view_cart')
        response.set_cookie('cart', json.dumps(cart))
        return response

def view_cart(request):
    cart = request.COOKIES.get('cart')
    cart = json.loads(cart) if cart else {}
    total = round(sum(item['total'] for item in cart.values()), 2)
    return render(request, 'cart/cart.html', {'cart': cart, 'total': total})

def remove_from_cart(request, product_id):
    cart = request.COOKIES.get('cart')
    cart = json.loads(cart) if cart else {}

    if str(product_id) in cart:
        if cart[str(product_id)]['quantity'] > 1:
            cart[str(product_id)]['quantity'] -= 1
            cart[str(product_id)]['total'] -= cart[str(product_id)]['price']
            cart[str(product_id)]['total'] = round(cart[str(product_id)]['total'], 2)
        else:
            del cart[str(product_id)]

    response = redirect('cart:view_cart')
    response.set_cookie('cart', json.dumps(cart))

    return response

def add_amount_to_cart(request, product_id, amount):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('/')
    

    if product.stock == 0:
        return redirect('/')
    else:
        cart = request.COOKIES.get('cart')
        cart = json.loads(cart) if cart else {}

        if product.stock - amount < 0 or (str(product_id) in cart and product.stock - cart[str(product_id)]['quantity'] - amount < 0):
            return redirect('/')

        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] += amount
            cart[str(product_id)]['total'] = round(cart[str(product_id)]['price'] * cart[str(product_id)]['quantity'], 2)
        else:
            cart[str(product_id)] = {
                "id": product_id,
                "name": product.name,
                "price": float(product.price),
                "quantity": amount,
                "total": float(round(product.price * amount, 2)),
                "image": product.image.url
            }

        response = redirect('/')
        response.set_cookie('cart', json.dumps(cart))
        messages.success(request, f'Has añadido {amount} unidades de {cart[str(product_id)]["name"]} a la cesta.')
        return response