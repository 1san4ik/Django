from django.shortcuts import render
from .models import Product


def templates(request):
    # tasks = Product.objects.order_by('-id')
    return render(request, 'third_app/product_info.html')
    # return render(request, 'third_app/product_info.html', {'text': tasks})
