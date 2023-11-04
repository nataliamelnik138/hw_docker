from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from courses.models import Course, Lesson, Payment, Subscription
from courses.paginator import CoursePaginator
from courses.permissions import IsModerator, IsOwner, IsSubscriber
from courses.serliazers import CourseSerializer, LessonSerializer, PaymentSerializer, \
    SubscriptionSerializer
from users.models import UserRoles


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    # def get_queryset(self):
    #     if not self.request.user.role == UserRoles.MODERATOR:
    #         queryset = Course.objects.filter(owner=self.request.user)
    #     else:
    #         queryset = Course.objects.all()
    #     return queryset

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'update' or self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    pagination_class = CoursePaginator

    def get_queryset(self):
        if not self.request.user.role == UserRoles.MODERATOR:
            queryset = Lesson.objects.filter(owner=self.request.user)
        else:
            queryset = Lesson.objects.all()
        return queryset


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'method')
    ordering_fields = ('date',)
    permission_classes = [IsAuthenticated]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer, *args, **kwargs):
        new_subscription = serializer.save()
        new_subscription.user = self.request.user
        pk = self.kwargs.get('pk')
        new_subscription.course = Course.objects.get(pk=pk)
        new_subscription.save()


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated, IsSubscriber]
