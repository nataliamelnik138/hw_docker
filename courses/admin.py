from django.contrib import admin

from courses.models import Lesson, Course, Subscription


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'course', 'owner')


@admin.register(Course)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',  'owner')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user',  'course', 'is_activ')
