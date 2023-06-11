from django.core.mail import send_mail

from config import settings


def send_order_email():
    send_mail(
        'Проверка',
        f'да',
        settings.EMAIL_HOST_USER,
        ['sir.iakowlew-pawel@yandex.ru'],
        fail_silently=False,

    )
# send_mail(
#     "Subject here",
#     "Here is the message.",
#     "from@example.com",
#     ["to@example.com"],
#     fail_silently=False,
# )