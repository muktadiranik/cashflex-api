from django.contrib.auth import get_user_model
from config import celery_app
from celery import shared_task
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import send_mail
import environ
User = get_user_model()
env = environ.Env()


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()


@shared_task
def send_mail_for_password_reset(email, token, first_name):
    context = {
        "password_reset_url": f"{env('FRONTEND_URL')}/reset-password/{token}",
        "first_name": first_name,
    }
    html_message = render_to_string("emails/password_reset_email.html", context)
    send_mail(
        subject='Cashflex Password Reset',
        message="Cashflex Password Reset Link",
        html_message=html_message,
        from_email=env("DEFAULT_FROM_NAME"),
        recipient_list=[email],
        fail_silently=False,
    )
