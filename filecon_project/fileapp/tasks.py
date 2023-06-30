from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from docx2pdf import convert
@shared_task
def sleepy(duration):
    sleep(5)
    return None



@shared_task
def send_mail_task_with_celery():
    send_mail(
        "Celery worked yeah",
        "sending mail using celery.",
        "prakashpatilmeti@gmail.com",
        ["prakashpatilmeti@gmail.com"],
        fail_silently=False,
    )
    print("Mail from celery")
    return None


@shared_task
def convert_doc_to_pdf(filename):
    convert('hotels/static/' + filename)
    return None