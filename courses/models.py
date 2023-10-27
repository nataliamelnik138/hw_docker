from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview_image = models.ImageField(
        upload_to='course_images/',
        verbose_name='Изображение',
        null=True,
        blank=True
    )
    description = models.TextField(verbose_name='описание')

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
    link_to_video = models.TextField(verbose_name='ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='lesson')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
