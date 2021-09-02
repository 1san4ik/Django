from django.db import models


class Task(models.Model):
    objects = None
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
