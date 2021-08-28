from django.shortcuts import render


def templates(request):
    return render(request, 'third_app/home.html')
