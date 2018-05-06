from django     import forms

from .models    import *


class UserForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['first_name'     ,
                  'last_name'      ,
                  'address_street' ,
                  'address_suburb' ,
                  'address_state'  ,
                  'address_postcode']


class ContactForm(forms.ModelForm):
    class Meta:
        model   = Contact
        exclude = ['user']


class DogForm(forms.ModelForm):
    class Meta:
        model  = Dog
        fields = '__all__'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model  = Appointment
        fields = '__all__'
