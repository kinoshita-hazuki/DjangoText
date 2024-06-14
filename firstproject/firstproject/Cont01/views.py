from django.http import HttpResponse
from django.shortcuts import render

def input_view(request):
    return render(request, 'input.html')

def form_view(request):
    user = request.GET.get('user', '')
    address = request.GET.get('address', '')
    userlen = len(user)
    addrlen = len(address)

    context = {
        'user': user,
        'address': address,
        'userlen': userlen,
        'addrlen': addrlen,
    }
    return render(request, 'form.html',context)
