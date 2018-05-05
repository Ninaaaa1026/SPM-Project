from datetime                       import datetime

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

