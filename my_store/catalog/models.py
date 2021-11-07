from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        'Название',
        max_length=150,
        help_text='max 150 символов'
    )
    slug = models.SlugField(
        'Слаг',
        max_length=150,
        help_text='max 150 символов'
    )
    weight = models.PositiveSmallIntegerField(
        'Порядок (чем меньше, тем выше).',
        default=100,
        help_text='Max 32767'
    )

    class Meta:
        ordering = ('weight', 'id')
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        'Название',
        max_length=200,
        unique=True
    )
    slug = models.SlugField(
       'Слаг',
       max_length=200,
       unique=True
    )

    class Meta:
        ordering = ('slug',)
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        default_related_name = 'tags'

    def __str__(self):
        return self.name


class Item(models.Model):
    is_on_main = models.BooleanField(
        'На главную?',
        default=False
    )
    name = models.CharField(
        'Название',
        max_length=150,
        help_text='max 150 символов'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        # related_name='items',
        verbose_name='Категория',
        help_text='Выберите категорию'
    )
    tags = models.ManyToManyField(Tag)
    text = models.TextField(
        'Описание',
        help_text='Напишите, насколько оно классное'
    )

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        default_related_name = 'items'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'catalog:item_detail',
            args=[str(self.pk)]
        )
