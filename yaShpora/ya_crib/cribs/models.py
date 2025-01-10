from datetime import datetime

from django.db import models


class Lesson(models.Model):
    sprint_number = models.IntegerField(
        verbose_name='Номер спринта')
    sprint_name = models.CharField(
        max_length=256,
        verbose_name='Название спринта')
    topic = models.CharField(
        max_length=256,
        verbose_name='Тема')
    lesson_number = models.IntegerField(
        verbose_name='Номер урока')
    
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
    
    def __str__(self):
        return (
            f'{self.topic}, урок {self.lesson_number}'
        )


class Crib(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
    )
    crib = models.FileField(upload_to='uploads/')
    lesson = models.ForeignKey(
        Lesson,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Урок',
        related_name='lesson'
    )

    class Meta:
        verbose_name = 'Шпора'
        verbose_name_plural = 'Шпоры'

