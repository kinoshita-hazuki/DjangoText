from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'home.html')

def hello_view(request):
    context = {'greeting': 'こんにちは、SpringMVC!'}
    return render(request, 'hello.html', context)

def input_view(request):
    return render(request, 'input.html')

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
        return render(request, 'form.html', context)
    return HttpResponse("Invalid request")

def foobar_view(request):
    return render(request, 'foobar.html')
