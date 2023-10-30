from django.conf import settings
from django.db import models

from users.models import User


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview_image = models.ImageField(
        upload_to='course_images/',
        verbose_name='Изображение',
        null=True,
        blank=True
    )
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview_image = models.ImageField(
        upload_to='course_images/',
        verbose_name='Изображение',
        null=True,
        blank=True
    )
    description = models.TextField(verbose_name='описание')
    link_to_video = models.URLField(verbose_name='ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='lesson')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment')
    date = models.DateField(verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='payment')
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True, related_name='payment')
    amount = models.FloatField(verbose_name='сумма оплаты')
    method = models.CharField(max_length=150,verbose_name='сумма оплаты')

    def __str__(self):
        return f'{self.pk} {self.date}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
