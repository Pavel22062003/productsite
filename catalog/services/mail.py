from config import settings

from django.core.mail import send_mail
def send_order_email():
    send_mail(
        'Проверка',
        f'да',
        settings.EMAIL_HOST_USER,
        ['mr.sergei2233@yandex.ru'],
        fail_silently=False,

    )