"""Модели приложения items."""
from django.db import models


class Gamer(models.Model):
    """Модель игрока."""
    username = models.CharField(
        'Ник персонажа',
        max_length=150,
        unique=True
    )
    haddan_id = models.IntegerField(
        'ID персонажа',
        unique=True
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def __str__(self):
        return self.username


class Wear(models.Model):
    """Модель шмотки."""
    gamer = models.ForeignKey(
        Gamer,
        on_delete=models.CASCADE,
        verbose_name='Игрок',
    )
    item_id = models.IntegerField(
        'S/N вещи',
        unique=True
    )
    item_type = models.CharField(
        'Тип шмотки',
        max_length=50
    )
    article = models.SmallIntegerField(
        'Артикул шмотки'
    )
    href = models.URLField(
        'Ссылка на шмотку'
    )

    class Meta:
        ordering = ('item_type',)
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'

    def __str__(self):
        return self.item_id


class GamerWear(models.Model):
    """Модель шмота игрока."""
    gamer = models.ForeignKey(
        Gamer,
        on_delete=models.CASCADE,
        verbose_name='Игрок',
        related_name='gamers'
    )
    wear = models.ForeignKey(
        Wear,
        on_delete=models.CASCADE,
        verbose_name='Вещь игрока',
        related_name='wears'
    )

    class Meta:
        ordering = ('gamer',)
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def __str__(self):
        return self.gamer
