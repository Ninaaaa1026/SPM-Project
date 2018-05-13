from datetime                       import datetime, timedelta, date, time

from django.contrib.auth            import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http                    import HttpResponseRedirect, HttpResponse
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
            if user.is_superuser:
                return HttpResponseRedirect('/groomer_home')
            else:
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

@login_required
def profile_view(request):
    user           = User       .objects.get   (email__exact = request.user.email           )
    contact_mobile = Contact    .objects.filter(user         = user, contact_type = 'mobile')
    contact_home   = Contact    .objects.filter(user         = user, contact_type = 'home'  )
    contact_work   = Contact    .objects.filter(user         = user, contact_type = 'work'  )
    dogs           = Dog        .objects.filter(owner        = user                         )
    appointments   = Appointment.objects.filter(subscriber   = user                         )
    breeds         = DOG_TYPE
    groom_types    = GROOM_TYPE
    return render(request, 'profile.html', {'user'          : user                                                                 ,
                                            'mobile'        : contact_mobile.get().phone_number if contact_mobile.exists() else '' ,
                                            'home'          : contact_home  .get().phone_number if contact_home  .exists() else '' ,
                                            'work'          : contact_work  .get().phone_number if contact_work  .exists() else '' ,
                                            'dogs'          : dogs                                                                 ,
                                            'appointments'  : appointments                                                         ,
                                            'breeds'        : breeds                                                               ,
                                            'groom_types'   : groom_types                                                          })

@login_required
def profile_update_view(request):
    profile_form = UserForm(request.POST)
    if profile_form.is_valid():
        user                    = User.objects.get(email = request.user.email)
        user.first_name         = profile_form.cleaned_data['first_name'      ]
        user.last_name          = profile_form.cleaned_data['last_name'       ]
        user.address_street     = profile_form.cleaned_data['address_street'  ]
        user.address_suburb     = profile_form.cleaned_data['address_suburb'  ]
        user.address_state      = profile_form.cleaned_data['address_state'   ]
        user.address_postcode   = profile_form.cleaned_data['address_postcode']
        user.address_country    = 'Australia'
        user.save()
        return HttpResponse(status = 201)
    else:
        return HttpResponse(status = 406)

@login_required
def contact_update_view(request):
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        contacts = Contact.objects.filter(user = request.user, contact_type = contact_form.cleaned_data['contact_type'])
        if not contacts.exists():
            Contact.objects.create(user         = request.user,
                                   contact_type = contact_form.cleaned_data['contact_type'],
                                   phone_number = contact_form.cleaned_data['phone_number'])
        else:
            contact              = Contact.objects.get(user         = request.user,
                                                       contact_type = contact_form.cleaned_data['contact_type'])
            contact.contact_type = contact_form.cleaned_data['contact_type']
            contact.phone_number = contact_form.cleaned_data['phone_number']
            contact.save()
        return HttpResponse(status = 201)
    else:
        return HttpResponse(status = 406)

@login_required
def dog_update_view(request):
    dog_form = DogForm(request.POST)
    if dog_form.is_valid():
        dogs = Dog.objects.filter(owner = request.user, id = request.POST.get('id'))
        if not dogs.exists():
            Dog.objects.create(owner         = request.user,
                               dog_name      = dog_form.cleaned_data['dog_name'     ],
                               breed         = dog_form.cleaned_data['breed'        ],
                               date_of_birth = dog_form.cleaned_data['date_of_birth'])
        else:
            dog               = Dog.objects.get(owner = request.user, id = request.POST.get('id'))
            dog.dog_name      = dog_form.cleaned_data['dog_name'     ]
            dog.breed         = dog_form.cleaned_data['breed'        ]
            dog.date_of_birth = dog_form.cleaned_data['date_of_birth']
            dog.save()
        return HttpResponse(status = 201)
    else:
        return HttpResponse(status = 406)

@login_required
def groomer_view(request):
    ##get made appointments
    #appointment_list = list(Appointment.objects.all())
    show = Appointment.objects.filter(appointment_datetime__date__gt=datetime.today()).select_related('subscriber__first_name'    ,
                                                                                                      'subscriber__address_street',
                                                                                                      'subscriber__address_suburb')
    #clientdets = User.objects.all().values('first_name','address_street','address_suburb')
    #
    query = show.values('subscriber__first_name','groom_dog','groom_type','comment',
                        'appointment_datetime','subscriber__address_street','subscriber__address_suburb')
    return render(request, 'groomer_home.html', {'events':query})

@login_required
def appointment_update_view(request):
    if request.method == 'POST':
        user = User.objects.get(email__exact=request.user.email)
        firstname = request.user.first_name
        action = request.POST.get('action')
        if action == 'add':
            appointment_form = AppointmentForm(request.POST)
            if appointment_form.is_valid():
                Appointment.objects.create(subscriber = appointment_form.cleaned_data['subscriber'],
                                           groom_dog = appointment_form.cleaned_data['groom_dog'],
                                           groom_type = appointment_form.cleaned_data[' groom_type'],
                                           order_price = appointment_form.cleaned_data['order_price'],
                                           payment_status = appointment_form.cleaned_data['payment_status '],
                                           comment = appointment_form.cleaned_data['comment '],
                                           appointment_datetime = appointment_form.cleaned_data['appointment_datetime'],
                                           appointment_statue =  appointment_form.cleaned_data['appointment_statue'])
                appointments = Appointment.objects.filter(subscriber=user)
                return render(request, 'appointment_list.html',
                              {'user': user, 'appointments': appointments, 'firstname': firstname})
            else:
                return render(request, 'appointment_add.html', {'errors': appointment_form.errors})
        elif action == 'update':
            appointment_form = AppointmentForm(request.POST)
            appointment_id = appointment_form.cleaned_data['id']
            if appointment_form.is_valid():
                appointment = Appointment.objects.get(id=appointment_id)
                appointment.appointment_datetime = appointment_form.cleaned_data['appointment_datetime']
                appointment.save()
                appointments=Appointment.objects.filter(subscriber=user)
                return render(request, 'appointment_list.html',
                              {'user': user, 'appointments': appointments, 'firstname': firstname})
            else:
                return render(request, 'appointment_edit.html', {'errors': appointment_form.errors})
        else:
            appointment_form = AppointmentForm(request.POST)
            appointment_id = appointment_form.cleaned_data['id']
            if appointment_form.is_valid():
                appointment = Appointment.objects.get(id=appointment_id)
                appointment.delete()
                appointments = Appointment.objects.filter(subscriber=user)
                return render(request, 'appointment_list.html',
                              {'user': user, 'appointments': appointments, 'firstname': firstname})
            else:
                return render(request, 'appointment_edit.html', {'errors': appointment_form.errors})

@login_required
def appointment_new_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(email__exact = request.user.email)
        dogs = Dog.objects.filter(owner=user)
        firstname = request.user.first_name
        available_datetimes = availabletime()
        return render(request, 'appointment_add.html', {'user': user,
                                                        'dogs': dogs,
                                                        'available_datetimes':available_datetimes,
                                                        'firstname': firstname})
    else:
        error = 'You have to sign in first.'
        return render(request, 'registration/login.html', {'error': error})

@login_required
def appointment_edit_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(email__exact = request.user.email)
            dogs = Dog.objects.filter(owner=user)
            appointment_form = AppointmentForm(request.POST)
            appointment_id = appointment_form.cleaned_data['id']
            appointment = Appointment.objects.get(id=appointment_id)
            firstname = request.user.first_name
            available_datetimes = availabletime()
            return render(request, 'appointment_edit.html', {'user': user,
                                                             'dogs': dogs,
                                                             'appointment': appointment,
                                                             'available_datetimes':available_datetimes,
                                                             'firstname': firstname})
    else:
        error = 'You have to sign in first.'
        return render(request, 'registration/login.html', {'error': error})

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
