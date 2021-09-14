from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from .models import Product
from django.contrib import messages
from django.contrib.auth import login, logout


def templates(request):
    name_product = Product.objects.all()
    context = {
        'PRODUCT': name_product
    }
    return render(request, 'third_app/product_info.html', context)


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



# class LoginView(CartMixin, View):
#
#     def get(self, request, *args, **kwargs):
#         form = LoginForm(request.POST or None)
#         category = Category.object.all()
#         context = {'form': form, 'category': category, 'cart': self.cart}
#         return render(request, 'login.html', context)
#
#     def post(self, request, *args, **kwargs):
#         form = LoginForm(request.POST or None)
#         if form.is_valid():
#             username = form.cleaned_data
#             password = form.cleaned_data
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#             return HttpResponseRedirect('templates')
#         return render(request, 'login.html', {'form': form, 'cart': self.cart})

# def add_to_cart(request, product_id, quantity):
#     product = Product.objects.get(id=product_id)
#     cart = Cart(request)
#     cart.add(product, product.unit_price, quantity)
#
# def remove_from_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     cart = Cart(request)
#     cart.remove(product)
#
# def get_cart(request):
#     return render_to_response('cart.html', dict(cart=Cart(request)))
