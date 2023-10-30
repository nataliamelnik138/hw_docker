from django.contrib import admin

from courses.models import Lesson, Course


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'course', 'owner')


@admin.register(Course)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',  'owner')
