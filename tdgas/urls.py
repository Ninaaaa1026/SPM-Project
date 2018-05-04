from django.urls 	import path

from .views 		import *

urlpatterns = [
	path(''      , home_view),
	path('signin', auth_views.login, name = 'login' ),
	path('signup', signup_view     , name = 'signup'),
	path('profile',profile_view, name = 'profile'),
	path('profile_update',profile_update_view, name = 'profile_update'),
	path('contact_update',contact_update_view, name = 'contact'),
	path('dog_update',dog_update_view, name = 'dog')
]