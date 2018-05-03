from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import *
from .models import *

from .models import DOG_TYPE

def home_view(request):
    firstname = ''
    if request.user.is_authenticated:
        firstname = request.user.first_name
    return render(request, 'home.html', {'firstname': firstname})

def signin_view(request):
    error = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username = email, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = 'Email or password not valid.'
    return render(request, 'registration/login.html', {'error': error})

def signup_view(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {})

def profile_view(request):
    if request.method == 'GET':
        dog_breeds = DOG_TYPE
        return render(request, 'user_profile.html', {'firstname': request.user.first_name,
                                                     'breeds'   : dog_breeds})
    if request.method == 'POST':
        pass

def dog_add_view(request):
    if request.method == 'POST':
        pass
    elif request.method == 'POST':
        signup_form = UserForm(request.POST)
        if signup_form.is_valid():
            newuser = signup_form.save()
            email = signup_form.cleaned_data.get('email')
            password = signup_form.cleaned_data.get('password')
            firstname = signup_form.cleaned_data.get('first_name')
            lastname = signup_form.cleaned_data.get('last_name')
            
            authenticate(email=email,password=password)
            login(request,newuser)
            #CustomUserManager.create_user(email,password)
            newuser = User(email=email, last_name=lastname, first_name=firstname, address_street=signup_form.cleaned_data['street_address'])
            newuser.save()

            return render(request, 'registration/update.html',{}) #HttpResponseRedirect('/', {'email':email})
        else:
            return render(request, 'registration/register.html', {})

def contact_dogs_view(request, username):
    if request.method == 'GET':
        return render(request, 'registration/update.html',{})
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data.get('number')
            ctype = form.cleaned_data.get('contact_type')
            contact = Contact(phone_number=number, contact_type=ctype)
            #check user in system and override 
            contact.save()

        return render(request, 'user_profile.html')
