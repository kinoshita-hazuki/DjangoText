from django.http import HttpResponse

def hellopythonfunc(request):
    responseobject = HttpResponse('<h1>hello python</h1>')
    setattr = HttpResponse('Pythonを楽しみましょう！')
    return responseobject