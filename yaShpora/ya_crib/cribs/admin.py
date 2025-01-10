from django.contrib import admin

from .models import Lesson, Crib

admin.site.empty_value_display = 'Не задано'


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'sprint_number',
        'topic',
        'lesson_number',
        'sprint_name',
    )
    list_editable = (
        'topic',
        'lesson_number',
        'sprint_name',
    )


class CribAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'crib',
        'lesson',
    )
    list_editable = (
        'description',
        'crib',
        'lesson',
    )


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Crib, CribAdmin)
