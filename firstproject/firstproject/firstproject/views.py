from django.http import HttpResponse

def firstproject(request):
    responseobject = HttpResponse('hello python')
    return responseobject