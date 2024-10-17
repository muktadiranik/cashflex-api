from django.contrib.auth import get_user_model
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import send_mail
import environ
env = environ.Env()
User = get_user_model()


@shared_task
def send_email_to_hr_on_company_create(username, email, password, uuid, domain):
    context = {
        'small_text_detail': 'We stongly recommend you to change your password after login.',
        'email': email,
        'username': username,
        'password': password,
        'domain': f"{domain}:{env('API_URL_PORT')}",
        'uuid': uuid,
    }
    message_html = render_to_string('emails/confirmation_email.html', context)
    send_mail(
        'Welcome to Cashflex',
        env("DEFAULT_FROM_NAME"),
        env("DEFAULT_FROM_EMAIL"),
        [email],
        html_message=message_html,
        fail_silently=False,
    )
