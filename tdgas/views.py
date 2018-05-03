from django.shortcuts import render
from .forms import UserForm, ContactForm, DogForm
from tdgas.models import User, Contact, Dog
import traceback

def home_view(request):
    return render(request, 'home.html', {'firstname': request.user.first_name})

def signup_view(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {})

def profile_view(request):
     return render(request, 'profile.html', {})

def profile_update_view(request):
    if request.method == 'POST':
        user = request.POST.get("username")
        profile = UserForm(request.POST)
        if profile.is_valid():
            try:
                p = User.objects.get(username = user)
                p.first_name = profile.cleaned_data['first_name']
                p.last_name = profile.cleaned_data['last_name']
                p.address_street = profile.cleaned_data['address_street']
                p.address_suburb = profile.cleaned_data['address_suburb']
                p.address_state = profile.cleaned_data['address_state']
                p.address_postcode = profile.cleaned_data['address_postcode']
                p.save()
            except:
                traceback.print_exc()
        else:
            profile.errors


def contact_update_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            contact = ContactForm(request.POST)
            if contact.is_valid():
                try:
                    p = Contact()
                    p.user = contact.cleaned_data['user']
                    p.contact_type = contact.cleaned_data['contact_type']
                    p.phone_number = contact.cleaned_data['phone_number']
                    p.save()
                except:
                    traceback.print_exc()
            else:
                contact.errors
        elif action == 'update':
            contact = ContactForm(request.POST)
            contact_id = contact.cleaned_data['id']
            if contact.is_valid():
                try:
                    p = Contact.objects.get(id = contact_id)
                    p.contact_type = contact.cleaned_data['contact_type']
                    p.phone_number = contact.cleaned_data['phone_number']
                    p.save()
                except:
                    traceback.print_exc()
            else:
                contact.errors
        else:
            contact = ContactForm(request.POST)
            contact_id = contact.cleaned_data['id']
            if contact.is_valid():
                try:
                    p = Contact.objects.get(id=contact_id)
                    p.delete()
                except:
                    traceback.print_exc()
            else:
                contact.errors

def dog_update_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            dog = DogForm(request.POST)
            if dog.is_valid():
                try:
                    p = Dog()
                    p.owner = dog.cleaned_data['owner']
                    p.dog_name = dog.cleaned_data['dog_name']
                    p.breed = dog.cleaned_data['breed']
                    p.date_of_birth = dog.cleaned_data['date_of_birth']
                    p.save()
                except:
                    traceback.print_exc()
            else:
                dog.errors
        elif action == 'update':
            dog = DogForm(request.POST)
            dog_id = dog.cleaned_data.get('id')
            if dog.is_valid():
                try:
                    p = Dog.objects.get(id = dog_id)
                    p.owner = dog.cleaned_data['owner']
                    p.dog_name = dog.cleaned_data['dog_name']
                    p.breed = dog.cleaned_data['breed']
                    p.date_of_birth = dog.cleaned_data['date_of_birth']
                    p.save()
                except:
                    traceback.print_exc()
            else:
                dog.errors
        else:
            dog = DogForm(request.POST)
            dog_id = dog.cleaned_data.get('id')
            if dog.is_valid():
                try:
                    p = Dog.objects.get(id = dog_id)
                    p.delete()
                except:
                    traceback.print_exc()
            else:
                dog.errors

