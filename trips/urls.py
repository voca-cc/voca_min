from django.urls import path, re_path
from .views import GetTrip, trip_registration


urlpatterns = [
    # path('', home, name='trips'),
    re_path(r'^trip/(?P<slug>[\w-]+)/$', GetTrip.as_view(), name='trip'),
    # re_path(r'^trip/trip/(?P<slug>[\w-]+)/$', VueTrip.as_view())
    re_path(r'registration/(?P<trip_slug>[\w-]+)/$', trip_registration, name='registration'),
    # re_path(r'thanks/$', thanks, name='thanks')
]
