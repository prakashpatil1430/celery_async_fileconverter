from django.core.mail import send_mail
from django.conf import settings

def send_mail_without_celery():
    subject = 'Sending mail'
    message = f'Hi sending mail without celery.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['prakashpatilmeti@gmail.com', ]
    
    send_mail( subject, message, email_from, recipient_list)
    return None
 