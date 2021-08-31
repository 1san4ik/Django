from django.shortcuts import render
from .models import Task


def templates(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'third_app/product_info.html', {'text': tasks})
