from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'Cont01/home.html')

def hello_view(request):
    context = {'greeting': 'Welcome to SpringMVC!'}
    return render(request, 'Cont01/hello.html', context)

def input_view(request):
    return render(request, 'Cont01/input.html')

def form_view(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        address = request.POST.get('address')
        userlen = len(user)
        addrlen = len(address)
        context = {
            'user': user,
            'userlen': userlen,
            'address': address,
            'addrlen': addrlen,
        }
        return render(request, 'Cont01/form.html', context)
    return HttpResponse("Invalid request")
