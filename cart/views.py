import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from product.models import Product

def add_to_cart(request, product_id):

    try:
        product = Product.objects.get(id=product_id)
        print(product.name)
    except Product.DoesNotExist:
        return redirect('cart:view_cart')

    product = {"id": product_id, "name": product.name, "price": float(product.price), "quantity": 1, "total": float(product.price)}
    cart = request.COOKIES.get('cart')
    cart = json.loads(cart) if cart else {}

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
        cart[str(product_id)]['total'] += cart[str(product_id)]['total']
    else:
        cart[str(product_id)] = product

    response = redirect('cart:view_cart')
    response.set_cookie('cart', json.dumps(cart))
    return response



def view_cart(request):
    cart = request.COOKIES.get('cart')
    cart = json.loads(cart) if cart else {}
    total = rounded_value = round(sum(item['total'] for item in cart.values()), 2)
    return render(request, 'cart/cart.html', {'cart': cart, 'total': total})


def remove_from_cart(request, product_id):
    cart = request.COOKIES.get('cart')
    cart = json.loads(cart) if cart else {}

    if str(product_id) in cart:
        if cart[str(product_id)]['quantity'] > 1:
            cart[str(product_id)]['quantity'] -= 1
        else:
            del cart[str(product_id)]

    response = redirect('cart:view_cart')
    response.set_cookie('cart', json.dumps(cart))

    return response