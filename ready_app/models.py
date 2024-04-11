from django.db import models


class MyDuffle(models.Model):  # Мое снаряжение.
    id_duffle = models.AutoField(primary_key=True)
    name_duffle = models.CharField(max_length=20, verbose_name='Наименование')
    heft = models.DecimalField(max_digits=4, decimal_places=2, null=True, verbose_name='Вес')
    expiration_date = models.DateField(null=True, blank=True, verbose_name='Срок годности')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, default=1)
    warehouse = models.ManyToManyField('Warehouse', default=1)

    class Meta:
        verbose_name = 'Снаряжение'
        verbose_name_plural = 'Снаряжение'
        ordering = ['id_duffle']


class Category(models.Model):  # Категория Дом, Огонь, медицина...
    id_category = models.AutoField(primary_key=True)
    name_category = models.CharField(max_length=20, verbose_name='Категория', default='Без категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id_category']


class Warehouse(models.Model):  # Склад. подвал/кладовая
    id_warehouse = models.AutoField(primary_key=True)
    name_waterhouse = models.CharField(max_length=20, verbose_name='Склад', default='Вне склада')

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        ordering = ['id_warehouse']


class Hike(models.Model):  # Для похода.
    id_duffle = models.ForeignKey(MyDuffle, on_delete=models.PROTECT, verbose_name='Поход')


class Bike(models.Model):  # Для велосипеда.
    id_duffle = models.ForeignKey(MyDuffle, on_delete=models.PROTECT, verbose_name='Велосипед')


class WaterRafting(models.Model):  # Для сплава.
    id_duffle = models.ForeignKey(MyDuffle, on_delete=models.PROTECT, verbose_name='Сплав')


class BP(models.Model):  # Для БП.
    id_duffle = models.ForeignKey(MyDuffle, on_delete=models.PROTECT, verbose_name='БП')
