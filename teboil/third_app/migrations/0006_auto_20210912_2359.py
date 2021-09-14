# Generated by Django 3.2.6 on 2021-09-12 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('third_app', '0005_auto_20210910_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Масло для строительной техники', 'Масло для строительной техники'), ('Трансмиссионное масло', 'Трансмиссионное масло'), ('Масло для мототехники', 'Масло для мототехники'), ('Моторное масло', 'Моторное масло'), ('Компрессорное масло', 'Компрессорное масло')], max_length=255, verbose_name='Название категории'),
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('qty', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='third_app.cart', verbose_name='Корзина')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
    ]
