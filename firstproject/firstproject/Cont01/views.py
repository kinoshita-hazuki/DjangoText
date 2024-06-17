from django.http import HttpResponse
from django.shortcuts import render
from django import forms

class SampleForm(forms.Form):
    user = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255)


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
