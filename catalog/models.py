from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    slug = models.CharField(max_length=100, **NULLABLE, verbose_name='Slug')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Изображение(превью)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}, {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    VERSION_CHOICES = ((True, 'активная'), (False, 'не активная'))

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(default=1, blank=True, verbose_name='Номер версии')
    version_name = models.CharField(max_length=250, verbose_name='Название версии')
    is_current = models.BooleanField(choices=VERSION_CHOICES, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.product} {self.version_number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('version_number',)  # сортировка по номеру версии
