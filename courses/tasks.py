import datetime

from celery import shared_task

from courses.services import send_mailing
from users.models import User


@shared_task
def send_email_about_course_updates(subscription):
    """
    Вызывает функцию, которая отправляет пользователю письмо
    об обновлении материалов курса
    :param subscription: подписка на курс
    """
    send_mailing(subscription)


@shared_task
def blocks_the_user():
    now = datetime.datetime.now()
    users = User.objects.filter(is_active=True)

    for user in users:
        if user.last_login:
            if user.last_login.timestamp() < (now - datetime.timedelta(days=30)).timestamp():
                user.is_active = False
                user.save()
                print(f"User {user.email} blocked")
