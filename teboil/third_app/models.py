from django.db import models
from django.contrib.auth import get_user_model, settings
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.db.models import CharField

User = get_user_model()


class Category(models.Model):

    MOTOR_OIL = 'Моторное масло'
    TRANSMISSION_OIL = 'Трансмиссионное масло'
    MOTORCYCLE_OIL = 'Масло для мототехники'
    OIL_FOR_MACHINERY = 'Масло для строительной техники'
    COMPRESSOR_OIL = 'Компрессорное масло'

    CHOISE_GROUP = {
        (MOTOR_OIL, 'Моторное масло'),
        (TRANSMISSION_OIL, 'Трансмиссионное масло'),
        (MOTORCYCLE_OIL, 'Масло для мототехники'),
        (OIL_FOR_MACHINERY, 'Масло для строительной техники'),
        (COMPRESSOR_OIL, 'Компрессорное масло'),
    }

    name = models.CharField(max_length=255, choices=CHOISE_GROUP, verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название товара', max_length=100)
    text = models.TextField(verbose_name='Описание', blank=True,)
    slug = models.SlugField(unique=True)
    image = models.ImageField(default='noimage.png', verbose_name='Изображение')
    availability = models.BooleanField(default=True, verbose_name='Наличие')

    approvals_certificates = models.CharField(max_length=255, blank=True, verbose_name='Допуски, сертификаты')
    density_at_20_C = models.CharField(max_length=50, blank=True, verbose_name='Плотность при 20°С')
    viscosity_at_40_C = models.CharField(max_length=50, blank=True, verbose_name='Вязкость при 40°С')
    viscosity_at_100_C = models.CharField(max_length=50, blank=True, verbose_name='Вязкость при 100°С')
    viscosity_at_minus_26_C = models.CharField(max_length=50, blank=True, verbose_name='Вязкость при -26°С')
    viscosity_at_minus_30_C = models.CharField(max_length=50, blank=True, verbose_name='Вязкость при -30°С')
    viscosity_index = models.CharField(max_length=50, blank=True, verbose_name='Индекс вязкости')
    flash_point = models.CharField(max_length=50, blank=True, verbose_name='Точка возгорания')
    pour_point = models.CharField(max_length=50, blank=True, verbose_name='Температура застывания')
    maximum_pumping_temp = models.CharField(max_length=50, blank=True, verbose_name='Предельная температура '
                                                                                   'перекачиваемости')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена (грн.)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар(ов)'


class Cart(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    total_product = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Корзина',
        verbose_name_plural = 'Корзина'


# class CartProduct(models.Model):
#
#     cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
#     # content_type = models.ForeignKey(ContentType, null=True, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     # content_object = GenericForeignKey('content_type', 'object_id')
#     qty = models.PositiveIntegerField(default=1)
#     # final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')
#
#     def __str__(self):
#         return f'Продукт {self.product.title} (для корзины) '
#
#     class Meta:
#         verbose_name = 'Товар в корзине'
#         verbose_name_plural = 'Товары в корзине'



class Customer(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Покупатель', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=50, verbose_name='Адрес')

    def __str__(self):
        return 'Покупатель: {} {}'.format(self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Status(models.Model):
    name_status = models.CharField(max_length=64, blank=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Статус {self.id, self.name_status}"

    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказа"



class Order(models.Model):
    customer_username = models.CharField(max_length=256, blank=True, default=None)
    customer_phone = models.CharField(max_length=64, blank=True, default=None)
    customer_email = models.EmailField(max_length=256, blank=True, default=None)
    comments = models.TextField(max_length=256, blank=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Заказ {self.id, self.status.name_status}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, default=None, on_delete=models.CASCADE)
    customer_username = models.CharField(max_length=256, blank=True, default=None)
    customer_phone = models.CharField(max_length=64, blank=True, default=None)
    customer_email = models.EmailField(max_length=256, blank=True, default=None)
    is_active = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
