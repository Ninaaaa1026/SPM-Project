from django import forms

from .models import *


class UserForm(forms.ModelForm):
    class Meta:
<<<<<<< HEAD
        model  = User
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model  = Contact
        fields = '__all__'
=======
        model = User
        fields = [
            'email',
            'password',
            'first_name',
            'last_name',
            'address_street',
            'address_suburb',
            'address_state',
            'address_postcode',
            'address_country'
        ]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'user',
            'contact_type',
            'phone_number'
        ]
>>>>>>> dev2_register


class DogForm(forms.ModelForm):
    class Meta:
<<<<<<< HEAD
        model  = Dog
        fields = '__all__'
=======
        model = Dog
        fields = [
            'owner',
            'dog_name',
            'breed',
            'date_of_birth'
        ]
>>>>>>> dev2_register


class AppointmentForm(forms.ModelForm):
    class Meta:
        model  = Appointment
        fields = '__all__'