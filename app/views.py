from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def home_view(request):
    
    return render(request, 'home.html', {'is_homepage': True})