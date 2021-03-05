from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView

from .forms import RegForm
from .models import Trip, Registration


# def home(request):
#     return render(request, 'trip.html', {
#         'trips':
#     })


class GetTrip(DetailView):
    model = Trip
    template_name = 'trip/trip.html'

    def get_context_data(self, **kwargs):
        ctx = super(GetTrip, self).get_context_data(**kwargs)
        return ctx


class VueTrip(DetailView):
    model = Trip
    template_name = 'trip/trip_new.html'

    def get_context_data(self, **kwargs):
        ctx = super(VueTrip, self).get_context_data(**kwargs)
        return ctx


def trip_registration(request, trip_slug):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.trip = Trip.objects.get(slug=trip_slug)
            registration.save()

            # return HttpResponseRedirect('thanks', social_links)
            return render(request, 'trip/thanks.html', {'social_links': {
                'instagram': registration.trip.owner.instagram_link,
                'facebook': registration.trip.owner.facebook_link,
                'vk': registration.trip.owner.vk_link,
                'telegram': registration.trip.owner.telegram_link,
            }})

    else:
        form = RegForm(auto_id=True)

    return render(request, 'trip/registration_trip.html', {'form': form})
