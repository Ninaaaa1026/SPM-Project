from datetime                       import datetime

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
            if user.is_superuser == True:
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
    user     = User.objects.get(email__exact = request.user.email)
    contacts = Contact.objects.filter(user = user)
    dogs     = Dog.objects.filter(owner = user)
    return render(request, 'profile.html', {'user': user, 'contacts': contacts, 'dogs': dogs})

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
            contact              = Contact.objects.get(user = request.user,
                                                       contact_type = contact_form.cleaned_data['contact_type'])
            contact.contact_type = contact_form.cleaned_data['contact_type']
            contact.phone_number = contact_form.cleaned_data['phone_number']
            contact.save()
        return HttpResponse(status = 201)
    else:
        return HttpResponse(status = 406)

@login_required
def dog_update_view(request):
    dog_form = ContactForm(request.POST)
    if dog_form.is_valid():
        dogs = Contact.objects.filter(owner = request.user, id = dog_form.cleaned_data['id'])
        if not dogs.exists():
            Dog.objects.create(owner         = request.user,
                               dog_name      = dog_form.cleaned_data['dog_name'     ],
                               breed         = dog_form.cleaned_data['breed'        ],
                               date_of_birth = dog_form.cleaned_data['date_of_birth'])
        else:
            dog               = Dog.objects.get(owner = request.user, id = dog_form.cleaned_data['id'])
            dog.dog_name      = dog_form.cleaned_data['dog_name'     ]
            dog.breed         = dog_form.cleaned_data['breed'        ]
            dog.date_of_birth = dog_form.cleaned_data['date_of_birth']
            dog.save()
        return HttpResponse(status = 201)
    else:
        return HttpResponse(status = 406)

