from django.contrib import admin

from courses.models import Lesson, Course, Subscription, Payment


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'course', 'owner')


@admin.register(Course)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',  'owner')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user',  'course', 'is_activ')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user',  'course', 'date', 'amount',)
