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

