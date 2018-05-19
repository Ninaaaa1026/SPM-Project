from django     import forms

from .models    import *


class UserForm(forms.ModelForm):
    class Meta:
        model  = User
        exclude = ['date_joined']


class ContactForm(forms.ModelForm):
    class Meta:
        model   = Contact
        exclude = ['user']
