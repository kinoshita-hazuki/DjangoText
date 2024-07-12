from django.shortcuts import render

def hellopythonfunc(request):
    context = {
        'greeting': 'Pythonを楽しみましょう！'
    }
    return render(request, 'hellopython.html', context)

