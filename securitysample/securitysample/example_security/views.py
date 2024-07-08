from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm

@login_required
def welcome(request):
    return render(request, 'example_security/welcome.html', {'user': request.user})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'example_security/login.html')

@login_required
def home_view(request):
    return render(request, 'example_security/home.html', {'user': request.user})