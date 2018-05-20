from __future__                     import absolute_import, unicode_literals
from celery                         import shared_task

import time as elapse_time

from django.template.loader         import get_template
from django.core.mail               import EmailMultiAlternatives
from django.db                      import connection
from datetime                       import datetime, timedelta

from .models                        import Appointment

def send_reminder_email(receiver, appointment):
    print('Sending out reminder email to ', receiver.first_name, ' at ', receiver.email, '...')
    subject, from_email, to = 'Tom\'s Grooming Service Appointment Reminder', 'ice.vilinon@gmail.com', [receiver.email]
    plain_content_template = get_template('html_emails/email_apt_confirm.txt')
    html_content_template = get_template('html_emails/email_apt_confirm.html')
    context = {'name': receiver.first_name, 'time': appointment.appointment_datetime}
    plain_content = plain_content_template.render(context)
    html_content = html_content_template.render(context)
    msg = EmailMultiAlternatives(subject, plain_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print('Reminder email sent.')

def check_reminder_email():
    print('Performing appointments reminder check...')
    now          = datetime.now() + timedelta(hours = 10)
    appointments = Appointment.objects.filter(reminded = False)
    for appointment in appointments:
        appointment_time = appointment.appointment_datetime
        time_delta       = appointment_time - now
        hour_delta       = (time_delta.days * 24) + (time_delta.seconds / 3600)
        if hour_delta <= 24:
            send_reminder_email(receiver    = appointment.subscriber,
                                appointment = appointment           )
            appointment.reminded = True
            appointment.save()
            connection.close()
        else:
            continue

@shared_task
def thread_check_reminder_email():
    while True:
        check_reminder_email()
        elapse_time.sleep(10)