import json

import django.http
from django.core import serializers

from .forms import EventForm
from .models import Event
from .serializer import EventSerializer


def get_all_event(request):
    # if request.method == 'POST':  # only true if form is submitted
    #     form = restapi.forms.CityForm(request.POST)  # add actual request data to form for processing
    #     form.save()
    event = Event.objects.all()
    serializ = EventSerializer(event, many=True)
    return django.http.JsonResponse(serializ.data, safe=False)

def create_event(request):
    form = EventForm(request)
    if not form.is_valid():
        return django.http.JsonResponse({'success': False, 'errors': form.errors})
    try:
        obj = form.save()
        return django.http.JsonResponse({'success': True})
    except django.db.utils.IntegrityError:
        return django.http.JsonResponse({'success': False, 'errors': ["An error occurred, please try again!"]})
