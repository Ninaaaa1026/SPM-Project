from django.urls import path

from .views import *

urlpatterns = [
	path(''       , home_view  ),
	path('signin' , signin_view , name = 'login' ),
	path('signup' , signup_view , name = 'signup'),
	path('profile', profile_view, name = 'user_profile'),
	path('<username>/update/', contact_dogs_view, name='update')
]