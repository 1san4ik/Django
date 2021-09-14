# Generated by Django 3.2.6 on 2021-09-16 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('third_app', '0008_auto_20210916_0348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer_username',
        ),
        migrations.AddField(
            model_name='order',
            name='customer_first_name',
            field=models.CharField(blank=True, default=None, max_length=256, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_last_name',
            field=models.CharField(blank=True, default=None, max_length=256, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='third_app.customer', verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Моторное масло', 'Моторное масло'), ('Масло для строительной техники', 'Масло для строительной техники'), ('Компрессорное масло', 'Компрессорное масло'), ('Трансмиссионное масло', 'Трансмиссионное масло'), ('Масло для мототехники', 'Масло для мототехники')], max_length=255, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Общая цена'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='third_app.customer', verbose_name='Логин'),
        ),
    ]
