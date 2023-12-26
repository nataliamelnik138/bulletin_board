from django.db import models

from users.models import User


class Advertisement(models.Model):
    title = models.CharField(max_length=200, verbose_name='название товара')
    price = models.IntegerField(null=True, blank=True, verbose_name='цена товара')
    description = models.TextField(verbose_name='описание товара', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', related_name='advertisements')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    image = models.ImageField(
        upload_to='ads/',
        blank=True,
        null=True,
        verbose_name='изображение'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'


class Review(models.Model):
    text = models.TextField(verbose_name='текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name='владелец')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='reviews',
                                      verbose_name='объявление')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
