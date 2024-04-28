from django.contrib.auth.models import User
from django.db import models
from pytils.translit import slugify


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')

    objects = models.Manager()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save()


class NewsPublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news', verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User, related_name='news', verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    objects = models.Manager()
    published = NewsPublishManager()

    class Meta:
        ordering = ['-updated']
        indexes = [
            models.Index(fields=['updated'])
        ]
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'{self.title}, {self.category}, {self.updated}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save()


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments', verbose_name='Новость')
    text = models.TextField(max_length=1000, verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    objects = models.Manager()

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['created'])
        ]
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.user}, {self.text}'

