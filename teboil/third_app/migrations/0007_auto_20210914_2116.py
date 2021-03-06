# Generated by Django 3.2.6 on 2021-09-14 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('third_app', '0006_auto_20210912_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_username', models.CharField(blank=True, default=None, max_length=256)),
                ('customer_phone', models.CharField(blank=True, default=None, max_length=64)),
                ('customer_email', models.EmailField(blank=True, default=None, max_length=256)),
                ('comments', models.TextField(blank=True, default=None, max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_username', models.CharField(blank=True, default=None, max_length=256)),
                ('customer_phone', models.CharField(blank=True, default=None, max_length=64)),
                ('customer_email', models.EmailField(blank=True, default=None, max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_status', models.CharField(blank=True, default=None, max_length=64)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Статус заказа',
                'verbose_name_plural': 'Статусы заказа',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Трансмиссионное масло', 'Трансмиссионное масло'), ('Масло для мототехники', 'Масло для мототехники'), ('Компрессорное масло', 'Компрессорное масло'), ('Моторное масло', 'Моторное масло'), ('Масло для строительной техники', 'Масло для строительной техники')], max_length=255, verbose_name='Название категории'),
        ),
        migrations.DeleteModel(
            name='CartProduct',
        ),
        migrations.AddField(
            model_name='productinorder',
            name='is_active',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='third_app.status'),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='order',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='third_app.order'),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='product',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='third_app.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='third_app.status'),
        ),
    ]
