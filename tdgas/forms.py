from django import forms

from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            email
            first_name
        ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = []


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = []


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = []