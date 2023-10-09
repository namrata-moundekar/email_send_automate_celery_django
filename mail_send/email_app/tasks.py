from datetime import date

from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Employee
from django.conf import settings




@shared_task
def send_event_emails():
    today = date.today()
    employees = Employee.objects.filter(birth_date__month=today.month, birth_date__day=today.day)

    for employee in employees:
        if employee.event_type == "birthday":
            subject = 'Happy Birthday!'
            html_message = render_to_string('birthday_template.html', {'emp_name': employee.name})
            from_email = settings.EMAIL_HOST_USER  # Your email address
            recipient_list = [employee.email_id]

            send_mail(subject, '', from_email, recipient_list, html_message=html_message)
        else:
            subject = 'Happy Anniversary!'
            html_message = render_to_string('anniversary_template.html', {'emp_name': employee.name})
            from_email = settings.EMAIL_HOST_USER  # Your email address
            recipient_list = [employee.email_id]

            send_mail(subject, '', from_email, recipient_list, html_message=html_message)

