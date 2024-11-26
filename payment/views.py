import json

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect, render

stripe.api_key = settings.STRIPE_SECRET_KEY


def payment_process(request):
    if 'HTTP_REFERER' not in request.META or 'cart' in request.META['HTTP_REFERER']:
        request.session['payment_step'] = 1
        request.session['payment_email'] = ''
        request.session['payment_address'] = {}
    
    step = request.session.get('payment_step', 1)
    
    if request.method == 'POST':
        if 'back' in request.POST:
            if step > 1:
                request.session['payment_step'] = step - 1
                return redirect('payment:process')
        
        elif step == 1:
            email = request.POST.get('email')
            if email:
                request.session['payment_email'] = email
                request.session['payment_step'] = 2
                return redirect('payment:process')
        
        elif step == 2:
            address = request.POST.get('address')
            country = request.POST.get('country')
            state = request.POST.get('state')
            postal_code = request.POST.get('postal_code')
            
            if all([address, country, state, postal_code]):
                request.session['payment_address'] = {
                    'address': address,
                    'country': country,
                    'state': state,
                    'postal_code': postal_code
                }
                return redirect('payment:create-checkout')

    progress_percentage = (step / 2) * 100
    
    context = {
        'step': step,
        'user': request.user,
        'stored_email': request.session.get('payment_email', ''),
        'stored_address': request.session.get('payment_address', {}),
        'progress_percentage': "width: " + str(progress_percentage) + "%"
    }
    return render(request, 'payment.html', context)


def create_checkout_session(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    cart = request.COOKIES.get('cart')
    cart = json.loads(cart) if cart else {}
    total = round(sum(item['total'] for item in cart.values()), 2)
    
    amount_in_cents = int(total * 100)
        
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'unit_amount': amount_in_cents,
                        'product_data': {
                            'name': 'Compra en EDB Electronics',
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri('/payment/success/'),
            cancel_url=request.build_absolute_uri('/payment/cancel/'),
        )
        return redirect(checkout_session.url)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def payment_success(request):
    cart = request.COOKIES.get('cart')
    cart = json.loads(cart) if cart else {}
    email = request.session.get('payment_email', '')
    address = request.session.get('payment_address', {})
    total = round(sum(item['total'] for item in cart.values()), 2)
    
    context = {
        'cart': cart,
        'email': email,
        'address': address,
        'total': total
    }
    
    response = render(request, 'success.html', context)
    response.delete_cookie('cart')
    return response

def payment_cancel(request):
    return render(request, 'cancel.html')
