from django.shortcuts import render, get_list_or_404
from .models import Category, Product

# Create your views here.
def product_list(request):
    departments = Category.objects.values('department', 'description', 'icon').distinct()
    context = {'departments': departments}
    return render(request, 'product/home.html', context)