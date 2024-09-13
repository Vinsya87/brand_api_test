from django.db import models


class Product(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=255)
    description = models.TextField(
        'Описание',
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
