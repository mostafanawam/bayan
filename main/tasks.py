# tasks.py (inside one of your Django apps)
from celery import shared_task

import logging


logger = logging.getLogger(__name__)


from django.core.mail import send_mail
from django.utils.html import strip_tags

from django.conf import settings



@shared_task()  
def send_email(subject,message,recipient_list):
    
    plain_message = strip_tags(message)
    send_mail(subject, plain_message, settings.EMAIL_HOST_USER, recipient_list,html_message=message)
    print('Email sent successfully!')

