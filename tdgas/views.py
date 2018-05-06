from datetime import datetime, timedelta, date, time

from django.contrib.auth            import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http                    import HttpResponseRedirect
from django.shortcuts               import render

from .forms                         import *
from .models                        import *

def home_view(request):
    firstname = ''
    if request.user.is_authenticated:
        firstname = request.user.first_name
    return render(request, 'home.html', {'firstname': firstname})

def signin_view(request):
    error = ''
    if request.method == 'POST':
        email    = request.POST.get('email')
        password = request.POST.get('password')
        user     = authenticate(username = email, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = 'Email or password not valid.'
    return render(request, 'registration/login.html', {'error': error})

def signup_view(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {})
    elif request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = User.objects.create(email       = user_form.cleaned_data['email'     ],
                                           password    = user_form.cleaned_data['password'  ],
                                           first_name  = user_form.cleaned_data['first_name'],
                                           last_name   = user_form.cleaned_data['last_name' ],
                                           date_joined = datetime.now())
            login(request, new_user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'registration/register.html', {'errors': user_form.errors})

### Review progress ###

@login_required
def profile_view(request):
    user     = User.objects.get(email__exact = request.user.email)
    contacts = Contact.objects.filter(user = user)
    dogs     = Dog.objects.filter(owner = user)
    return render(request, 'profile.html', {'user': user, 'contacts': contacts, 'dogs': dogs})

@login_required
def profile_update_view(request):
    if request.method == 'POST':
        user = request.POST.get("username")
        profile = UserForm(request.POST)
        if profile.is_valid():
            p = User.objects.get(username = user)
            p.first_name = profile.cleaned_data['first_name']
            p.last_name = profile.cleaned_data['last_name']
            p.address_street = profile.cleaned_data['address_street']
            p.address_suburb = profile.cleaned_data['address_suburb']
            p.address_state = profile.cleaned_data['address_state']
            p.address_postcode = profile.cleaned_data['address_postcode']
            p.save()
        else:
            profile.errors

@login_required
def contact_update_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            contact = ContactForm(request.POST)
            if contact.is_valid():
                p = Contact()
                p.user = contact.cleaned_data['user']
                p.contact_type = contact.cleaned_data['contact_type']
                p.phone_number = contact.cleaned_data['phone_number']
                p.save()
            else:
                contact.errors
        elif action == 'update':
            contact = ContactForm(request.POST)
            contact_id = contact.cleaned_data['id']
            if contact.is_valid():
                p = Contact.objects.get(id = contact_id)
                p.contact_type = contact.cleaned_data['contact_type']
                p.phone_number = contact.cleaned_data['phone_number']
                p.save()
            else:
                contact.errors
        else:
            contact = ContactForm(request.POST)
            contact_id = contact.cleaned_data['id']
            if contact.is_valid():
                p = Contact.objects.get(id=contact_id)
                p.delete()
            else:
                contact.errors
                
@login_required
def dog_update_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            dog = DogForm(request.POST)
            if dog.is_valid():
                p = Dog()
                p.owner = dog.cleaned_data['owner']
                p.dog_name = dog.cleaned_data['dog_name']
                p.breed = dog.cleaned_data['breed']
                p.date_of_birth = dog.cleaned_data['date_of_birth']
                p.save()
            else:
                dog.errors
        elif action == 'update':
            dog = DogForm(request.POST)
            dog_id = dog.cleaned_data.get('id')
            if dog.is_valid():
                p = Dog.objects.get(id = dog_id)
                p.owner = dog.cleaned_data['owner']
                p.dog_name = dog.cleaned_data['dog_name']
                p.breed = dog.cleaned_data['breed']
                p.date_of_birth = dog.cleaned_data['date_of_birth']
                p.save()
            else:
                dog.errors
        else:
            dog = DogForm(request.POST)
            dog_id = dog.cleaned_data.get('id')
            if dog.is_valid():
                p = Dog.objects.get(id = dog_id)
                p.delete()
            else:
                dog.errors

def appointment_update_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            appointment_form = AppointmentForm(request.POST)
            if appointment_form.is_valid():
                new_appointment = Appointment.objects.create(   subscriber = appointment_form.cleaned_data['subscriber'],
                                                                groom_dog = appointment_form.cleaned_data['groom_dog'],
                                                                groom_type = appointment_form.cleaned_data[' groom_type'],
                                                                order_price = appointment_form.cleaned_data['order_price'],
                                                                payment_status = appointment_form.cleaned_data['payment_status '],
                                                                comment = appointment_form.cleaned_data['comment '],
                                                                appointment_datetime = appointment_form.cleaned_data['appointment_datetime'],
                                                                create_datetime = appointment_form.cleaned_data['create_datetime'],
                                                                appointment_statue = 'TE')
                return render(request, 'appointment_list.html', {'appointment': new_appointment})
            else:
                return render(request, 'registration/register.html', {'errors': appointment_form.errors})
        elif action == 'update':
            appointment_form = AppointmentForm(request.POST)
            appointment_id = appointment_form.cleaned_data['id']
            if appointment_form.is_valid():
                p = Appointment.objects.get(id=appointment_id)
                p.appointment_datetime = appointment_form.cleaned_data['appointment_datetime']
                p.save()
            else:
                return render(request, 'appointment_list.html', {'errors': appointment_form.errors})
        else:
            appointment_form = AppointmentForm(request.POST)
            appointment_id = appointment_form.cleaned_data['id']
            if appointment_form.is_valid():
                p = Appointment.objects.get(id=appointment_id)
                p.delete()
            else:
                return render(request, 'appointment_list.html', {'errors': appointment_form.errors})

def appointment_new_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(email__exact = request.user.email)
        dogs = Dog.objects.filter(owner=user)
        firstname = request.user.first_name

        date_from = date.today()
        if date.today().weekday() == [0 - 3]:
            if datetime.now().hour < 8 & datetime.now().minute < 30:
                datetime_from_hour = 8
                datetime_from_minute = 30
            elif datetime.now().hour < 10:
                datetime_from_hour = 10
                datetime_from_minute = 0
            elif datetime.now().hour < 12 & datetime.now().minute < 30:
                datetime_from_hour = 12
                datetime_from_minute = 30
            elif datetime.now().hour < 14:
                datetime_from_hour = 14
                datetime_from_minute = 0
            elif datetime.now().hour < 15 & datetime.now().minute < 30:
                datetime_from_hour = 15
                datetime_from_minute = 30
            else:
                datetime_from_hour = 8
                datetime_from_minute = 30
                date_from = date.today() + timedelta(days=1)
        elif date.today().weekday() == 4:
            if datetime.now().hour < 8 & datetime.now().minute < 30:
                datetime_from_hour = 8
                datetime_from_minute = 30
            elif datetime.now().hour < 10:
                datetime_from_hour = 10
                datetime_from_minute = 0
            elif datetime.now().hour < 12 & datetime.now().minute < 30:
                datetime_from_hour = 12
                datetime_from_minute = 30
            elif datetime.now().hour < 14:
                datetime_from_hour = 14
                datetime_from_minute = 0
            elif datetime.now().hour < 15 & datetime.now().minute < 30:
                datetime_from_hour = 15
                datetime_from_minute = 30
            else:
                date_from = date.today() + timedelta(days=3)
                datetime_from_hour = 8
                datetime_from_minute = 30
        elif date.today().weekday() == 5:
            date_from = date.today() + timedelta(days=2)
            datetime_from_hour = 8
            datetime_from_minute = 30
        else:
            date_from = date.today() + timedelta(days=1)
            datetime_from_hour = 8
            datetime_from_minute = 30

        date_to = date_from + timedelta(days=7)
        date_slot = date_from

        time_from = time(datetime_from_hour, datetime_from_minute, 0, 0)
        time_slot = time_from

        available_datetimes = []

        while date_from <= date_slot <= date_to:
            if date_slot.weekday() != [5, 6]:
                    while time_from <= time_slot < time(11, 30, 0, 0) or time(12, 30, 0, 0)<=time_slot<= time(17, 0, 0, 0):
                        pre_available_time = datetime(date_slot.year, date_slot.month, date_slot.day, time_slot.hour,
                                                  time_slot.minute, 0)
                        if not Appointment.objects.filter(appointment_datetime__contains=pre_available_time):
                            available_datetimes.append(pre_available_time)
                            time_slot = time_slot + timedelta(minutes=90)
                        if time_slot==time(11, 30, 0, 0):
                            time_slot=time_slot + timedelta(minutes=60)
            date_slot = date_slot + timedelta(days=1)

        return render(request, 'appointment_add.html', {'user': user, 'dogs': dogs, 'available_datetimes':available_datetimes,'firstname': firstname})
    else:
        error = 'You have to sign in first.'
        return render(request, 'registration/login.html', {'error': error})

def appointment_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(email__exact = request.user.email)
        appointments = Appointment.objects.filter(subscriber=user)
        firstname = request.user.first_name
        if request.method == 'GET':
            return render(request, 'appointment_list.html', {'user': user, 'appointments': appointments, 'firstname': firstname})
    else:
        error = 'You have to sign in first.'
        return render(request, 'registration/login.html', {'error': error})
