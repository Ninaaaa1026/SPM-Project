import time as elapse_time
import threading

from django.template.loader         import get_template
from django.core.mail               import EmailMultiAlternatives
from django.db                      import connection

from datetime           import datetime, timedelta, date, time

from .models            import Appointment

MONDAY      =  0
TUESDAY     =  1
WEDNESDAY   =  2
THRUSDAY    =  3
FRIDAY      =  4
SATURDAY    =  5
SUNDAY      =  6
WORK_DAY    = [0, 1, 2, 3, 4]
WEEK_END    = [5, 6]

def available_time():
    date_from   = date.today()
    weekday     = date.today().weekday()
    now         = datetime.now() + timedelta(hours = 10) ### Australian Eastern Standard Time
    if weekday in WORK_DAY:
        if   time( 0,  0) <= now.time() < time( 8, 30):
            datetime_from_hour      = 8
            datetime_from_minute    = 30
        elif time( 8, 30) <= now.time() < time(10,  0):
            datetime_from_hour      = 10
            datetime_from_minute    = 0
        elif time(10,  0) <= now.time() < time(12, 30):
            datetime_from_hour      = 12
            datetime_from_minute    = 30
        elif time(12, 30) <= now.time() < time(14,  0):
            datetime_from_hour      = 14
            datetime_from_minute    = 0
        elif time(14,  0) <= now.time() < time(15, 30):
            datetime_from_hour      = 15
            datetime_from_minute    = 30
        else:
            datetime_from_hour      = 8
            datetime_from_minute    = 30
            date_from               = date.today() + timedelta(days = 3 if weekday == FRIDAY else 1)
    else:
        date_from               = date.today() + timedelta(days = 2 if weekday == SATURDAY else 1)
        datetime_from_hour      = 8
        datetime_from_minute    = 30

    date_from = datetime(date_from.year, date_from.month, date_from.day, datetime_from_hour, datetime_from_minute)
    date_to   = date_from + timedelta(days = 6)
    date_slot = date_from

    available_datetimes = []

    while date_from <= date_slot < date_to:
        if not date_slot.weekday() in WEEK_END:
            while time(8, 30) <= date_slot.time() <= time(16, 0):
                if not Appointment.objects.filter(appointment_datetime__contains = date_slot).exists():
                    if date_slot.time() == time(11, 30):
                        date_slot = date_slot + timedelta(minutes = 60)
                    available_datetimes.append(date_slot.strftime("%Y-%m-%d %H:%M"))
                date_slot = date_slot + timedelta(minutes = 90)
        date_slot = datetime(date_slot.year, date_slot.month, date_slot.day, 8, 30, 0)
        date_slot = date_slot + timedelta(days = 1)
    return available_datetimes

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
        hour_delta       = (appointment_time - now).seconds / 3600
        if hour_delta <= 24:

            send_reminder_email(receiver = appointment.subscriber, appointment = appointment)

            appointment.reminded = True
            appointment.save()
            connection.close()
        else:
            continue

def thread_task(function):
  def decorator():
    t = threading.Thread(target = function)
    t.daemon = True
    t.start()
  return decorator