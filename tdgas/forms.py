from django     import forms

from .models    import *


class UserForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['email', 'password', 'first_name', 'last_name']


class ContactForm(forms.ModelForm):
    class Meta:
        model  = Contact
        fields = '__all__'


class DogForm(forms.ModelForm):
    class Meta:
        model  = Dog
        fields = '__all__'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model  = Appointment
        fields = '__all__'
