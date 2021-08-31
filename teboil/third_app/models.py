from django.db import models


class Task(models.Model):
    objects = None
    title = models.CharField('Название', max_length=35)
    text = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Название Товара'
        verbose_name_plural = 'Названия Товаров'
