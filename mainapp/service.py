from core.settings import DEFAULT_FROM_EMAIL, EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import Subject


def send(**user):
    message = f"""Пользователь {user['user_name']}, хочет на курас {user['subject']}
       его номер {user['user_phone']} и почта {user['email']}"""
    send_mail(
        'Оповещение о ЗАПРОСАХ НА КУРС',
        message,
        EMAIL_HOST_USER,
        [DEFAULT_FROM_EMAIL],
        fail_silently=False
    )
