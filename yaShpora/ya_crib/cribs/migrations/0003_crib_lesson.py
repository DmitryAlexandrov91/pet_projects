# Generated by Django 4.2.16 on 2024-10-10 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cribs', '0002_lesson_remove_crib_lesson_remove_crib_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='crib',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cribs.lesson', verbose_name='Урок'),
        ),
    ]
