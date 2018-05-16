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
        fields = ['id', 'dog_name', 'breed', 'date_of_birth']


class AppointmentForm(forms.Form):
    dog_id               = forms.IntegerField   ()
    groom_type           = forms.CharField      (max_length = SHORT)
    appointment_datetime = forms.DateTimeField  (input_formats = ['%Y-%m-%d %H:%M:%S'])
    # comment = models.CharField(max_length = LONG, null = True, blank = True)
