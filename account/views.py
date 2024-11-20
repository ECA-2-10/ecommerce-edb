from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada con éxito.')
            return redirect('login')
        else:
            messages.error(request, 'Hubo un error al crear la cuenta.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'account/register.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "¡Nombre de usuario o contraseña inválidos!")
            return redirect('login')

    return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')