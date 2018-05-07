from django.contrib.auth.views  import logout
from django.urls                import path

from .views                     import *

urlpatterns = [
    path(''                     , home_view                                         ),
    path('login/'               , signin_view           , name = 'login'            ),
    path('logout/'              , logout                , {'next_page': '/'}        ),
    path('signup/'              , signup_view           , name = 'signup'           ),
    path('profile/'             , profile_view          , name = 'profile'          ),
    path('profile_update/'      , profile_update_view   , name = 'profile_update'   ),
    path('contact_update/'      , contact_update_view   , name = 'contact'          ),
    path('dog_update/'          , dog_update_view       , name = 'dog'              ),
    path('appointment/'			, appointment_view		, name = 'appointment'),
    path('appointment_new/'		, appointment_new_view	, name = 'appointment_new'),
	path('appointment_update/'	, appointment_update_view, name = 'appointment_update'),
    path('appointment_edit/'	, appointment_edit_view, name = 'appointment_edit')
]
