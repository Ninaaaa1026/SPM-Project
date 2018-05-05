from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None             , {'fields': ('email',
                                        'password')}),
        ('Personal info'  , {'fields': ('first_name',
                                        'last_name',
                                        'address_street',
                                        'address_suburb',
                                        'address_state',
                                        'address_postcode',
                                        'address_country')}),
        ('Permissions'    , {'fields': ('is_active',
                                        'is_staff',
                                        'is_superuser',
                                        'groups',
                                        'user_permissions')}),
        ('Important dates', {'fields': ('last_login',
                                        'date_joined')}),
    )
    add_fieldsets = (
        (None             , {'classes': ('wide',),
                             'fields' : ('email', 'password1', 'password2')}),
    )
    list_display  = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering      = ('email',)

# Register your models below.
admin.site.register(Contact)
admin.site.register(Dog)
admin.site.register(Appointment)