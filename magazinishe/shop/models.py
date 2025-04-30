from django.db import models

# Create your models here.

MAX_LENGTH = 255

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name = 'Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Collection(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name = 'Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекция'

class Clothes(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name = 'Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    color = models.CharField(max_length = MAX_LENGTH, verbose_name='Цвет')
    min_size = models.PositiveIntegerField(default=36, verbose_name='Минимальный размер')
    max_size = models.PositiveIntegerField(default=52, verbose_name='Максимальный размер')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exist = models.BooleanField(default=True, verbose_name='В наличии')

    collection = models.ManyToManyField(Collection, verbose_name='Коллекция')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    

    def __str__(self):
        return f'{self.name} - {self.price} руб.'
    
    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'