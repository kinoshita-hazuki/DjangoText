from django.http import HttpResponse
from django.shortcuts import render

def input_view(request):
    return render(request, 'input.html')

def form_view(request):
    return render(request, 'form.html')
