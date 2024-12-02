from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from order.models import Order

def order_search(request):
    context = {}
    if request.method == "POST":
        order_code = request.POST.get("order_code", "").strip()
        if order_code:
            try:
                # Busca el pedido en la base de datos
                order = Order.objects.get(code=order_code)
                # Incluye los productos relacionados
                order_products = order.order_products.select_related('product')
                context["order"] = order
                context["order_products"] = order_products
            except Order.DoesNotExist:
                context["error"] = "Order not found."
    return render(request, "order/order_search.html", context)


def order_from_email(request):
    order_code = request.GET.get('order_code')
    
    # Renderizamos una página que automáticamente enviará un formulario POST
    context = {
        'order_code': order_code,
    }

    return render(request, 'order/order_from_email.html', context)