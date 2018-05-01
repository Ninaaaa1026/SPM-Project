from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

urlpatterns = [
	path(''      , home_view),
	path('signin', auth_views.login, name = 'login' ),
	path('signup', signup_view	   , name = 'signup'),
]