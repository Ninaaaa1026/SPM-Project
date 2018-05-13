from django.contrib.auth.views  import logout
from django.urls                import path

from .views                     import *

urlpatterns = [
    path(''                     , home_view                                                 ),
    path('logout/'              , logout                    , {'next_page': '/'}            ),
    path('login/'               , signin_view               , name = 'login'                ),
    path('signup/'              , signup_view               , name = 'signup'               ),
    path('profile/'             , profile_view              , name = 'profile'              ),
    path('profile_update/'      , profile_update_view       , name = 'profile_update'       ),
    path('contact_update/'      , contact_update_view       , name = 'contact'              ),
    path('dog_update/'          , dog_update_view           , name = 'dog'                  ),
    path('appointment_new/'		, appointment_update_view	, name = 'appointment_update'   ),
	path('appointment_update/'	, appointment_delete_view   , name = 'appointment_delete'   ),

    path('groomer_home/'        , groomer_view              , name = 'groomer'              )
]
