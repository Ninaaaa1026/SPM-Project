from django import forms

from .models import *


class UserForm(forms.ModelForm):
    class Meta:
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


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = [
            'owner',
            'dog_name',
            'breed',
            'date_of_birth'
        ]


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = []