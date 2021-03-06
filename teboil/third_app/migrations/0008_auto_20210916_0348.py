# Generated by Django 3.2.6 on 2021-09-16 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('third_app', '0007_auto_20210914_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinorder',
            name='customer_email',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='customer_phone',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='customer_username',
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_address',
            field=models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='third_app.customer'),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='nmb',
            field=models.IntegerField(default=1, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='price_per_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена за шт.'),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Общая цена'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Компрессорное масло', 'Компрессорное масло'), ('Масло для строительной техники', 'Масло для строительной техники'), ('Трансмиссионное масло', 'Трансмиссионное масло'), ('Моторное масло', 'Моторное масло'), ('Масло для мототехники', 'Масло для мототехники')], max_length=255, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comments',
            field=models.TextField(blank=True, default=None, max_length=256, verbose_name='Комментарии'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_email',
            field=models.EmailField(blank=True, default=None, max_length=256, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_phone',
            field=models.CharField(blank=True, default=None, max_length=64, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_username',
            field=models.CharField(blank=True, default=None, max_length=256, verbose_name='Покупатель'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='third_app.status', verbose_name='Статус заказа'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='is_active',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='third_app.status', verbose_name='Вкл.'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='order',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='third_app.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='product',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='third_app.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='status',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Включен'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name_status',
            field=models.CharField(blank=True, default=None, max_length=64, verbose_name='Статус заказа'),
        ),
    ]
