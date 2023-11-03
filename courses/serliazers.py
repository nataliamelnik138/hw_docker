from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from courses.models import Course, Lesson, Payment, Subscription
from courses.validators import LinkToVideoValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            LinkToVideoValidator(field='link_to_video')
        ]


class CourseSerializer(serializers.ModelSerializer):
    number_of_lessons = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)
    signed = SerializerMethodField()

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_signed(self, course):
        user = self.context['request'].user
        if Subscription.objects.filter(course=course).filter(user=user):
            return True
        return False

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'preview_image', 'number_of_lessons', 'owner', 'lesson', 'signed',)


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
