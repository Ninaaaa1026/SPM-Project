from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *

def home_view(request):
    return render(request, 'home.html') #{'firstname': request.user.first_name})

def signup_view(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {})
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

def signin_view(request,first_name):
    if request.method =='POST':
        #authenticate and return to home page

        return render(request, 'home.html', {firstname:first_name})