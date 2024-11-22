from django.shortcuts import render

from .models import Category, Department, Product


def product_list(request):
    category_name = request.GET.get('category')
    department_name = request.GET.get('department')
    search_query = request.GET.get('search')
    
    products = Product.objects.all()
    
    if category_name:
        products = products.filter(category__name=category_name)
    
    if department_name and department_name != "Todos los departamentos":
        products = products.filter(category__department__name=department_name)
    
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    categories = Category.objects.all()
    departments = Department.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'departments': departments,
    }
    
    return render(request, 'product/home.html', context)