from datetime import datetime, timedelta, date, time

def availabletime():
    date_from = date.today()
    weekday=date.today().weekday()
    if weekday == 0 or weekday == 1 or weekday == 2 or weekday ==3:
        if time(0,0,0,0)<=datetime.now().time()<time(8,30,0,0):
            datetime_from_hour = 8
            datetime_from_minute = 30
        elif time(8,30,0,0)<=datetime.now().time()<time(10,0,0,0):
            datetime_from_hour = 10
            datetime_from_minute = 0
        elif time(10,0,0,0)<=datetime.now().time()<time(12,30,0,0):
            datetime_from_hour = 12
            datetime_from_minute = 30
        elif time(12,30,0,0)<=datetime.now().time()<time(14,0,0,0):
            datetime_from_hour = 14
            datetime_from_minute = 0
        elif time(14,0,0,0)<=datetime.now().time()<time(15,30,0,0):
            datetime_from_hour = 15
            datetime_from_minute = 30
        else:
            datetime_from_hour = 8
            datetime_from_minute = 30
            date_from = date.today() + timedelta(days=1)
    elif weekday == 4:
        if time(0,0,0,0)<=datetime.now().time()<time(8,30,0,0):
            datetime_from_hour = 8
            datetime_from_minute = 30
        elif time(8,30,0,0)<=datetime.now().time()<time(10,0,0,0):
            datetime_from_hour = 10
            datetime_from_minute = 0
        elif time(10,0,0,0)<=datetime.now().time()<time(12,30,0,0):
            datetime_from_hour = 12
            datetime_from_minute = 30
        elif time(12,30,0,0)<=datetime.now().time()<time(14,0,0,0):
            datetime_from_hour = 14
            datetime_from_minute = 0
        elif time(14,0,0,0)<=datetime.now().time()<time(15,30,0,0):
            datetime_from_hour = 15
            datetime_from_minute = 30
        else:
            date_from = date.today() + timedelta(days=3)
            datetime_from_hour = 8
            datetime_from_minute = 30
    elif weekday == 5:
        date_from = date.today() + timedelta(days=2)
        datetime_from_hour = 8
        datetime_from_minute = 30
    else:
        date_from = date.today() + timedelta(days=1)
        datetime_from_hour = 8
        datetime_from_minute = 30

    date_from = datetime(date_from.year, date_from.month, date_from.day, datetime_from_hour, datetime_from_minute,0)
    date_to = date_from + timedelta(days=6)
    date_slot = date_from

    available_datetimes = []

    while date_from <= date_slot < date_to:
        if date_slot.weekday() != 6 and date_slot.weekday() != 5:
            while time(8, 30, 0, 0) <= date_slot.time() < time(11, 30, 0, 0) or time(12, 30, 0, 0)<=date_slot.time()<= time(15, 30, 0, 0):
                if not Appointment.objects.filter(appointment_datetime__contains=date_slot):
                    available_datetimes.append(date_slot)
                    date_slot = date_slot + timedelta(minutes=90)
                if date_slot.time()==time(11, 30, 0, 0):
                    date_slot=date_slot + timedelta(minutes=60)
        date_slot = date_slot + timedelta(days=1)
        date_slot = datetime(date_slot.year,date_slot.month,date_slot.day,8,30,0)
    return available_datetimes
