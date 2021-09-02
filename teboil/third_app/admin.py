from django.contrib import admin
from .models import Category, CartProduct, Cart, Customer, MotorOilsForCars, TransmissionOils

admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(MotorOilsForCars)
admin.site.register(TransmissionOils)
