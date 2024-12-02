from django.shortcuts import render

from .models import Category, Department, Product


def product_list(request):
    category_name = request.GET.get('category')
    department_name = request.GET.get('department')
    maker_name = request.GET.get('maker')
    search_query = request.GET.get('search')
    
    products = Product.objects.all()
    
    if category_name:
        products = products.filter(category__name=category_name)
    
    if department_name and department_name != "Todos los departamentos":
        products = products.filter(category__department__name=department_name)

    #print(f'"{request.GET}"')
    if maker_name and maker_name != "Todos los fabricantes":
        products = products.filter(maker__icontains=maker_name)
        print(products)
    
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    categories = Category.objects.all()
    departments = Department.objects.all()
    makers = Product.objects.values('maker').distinct()

    print(products)
    context = {
        'products': products,
        'categories': categories,
        'departments': departments,
        'makers': makers
    }
    
    return render(request, 'product/home-better.html', context)