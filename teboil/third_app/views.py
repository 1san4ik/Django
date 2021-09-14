from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from .models import Product
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views.generic import ListView


def templates(request):
    name_product = Product.objects.all()
    context = {
        'PRODUCT': name_product
    }
    return render(request, 'third_app/product_info.html', context)


def categoryshow(request, product_id):
    category_item = Category.objects.get(id=product_id)
    category_name = Category.objects.all()
    context = {
        'CATEGORY': category_name
    }
    return render(request, 'third_app/category.html', locals())



def productshow(request, product_id):
    product_item = Product.objects.get(id=product_id)
    product_name = Product.objects.all()
    context = {
        'PRODUCT': product_name
    }
    return render(request, 'third_app/product_show.html', locals())


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('templates')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'third_app/registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('templates')
    else:
        form = UserLoginForm()
    return render(request, 'third_app/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


class Search(ListView):

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context
