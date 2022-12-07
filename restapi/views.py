import django.http
from rest_framework import viewsets



from .models import Event
from .serializer import EventSerializer
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# def get_all_event(request):
#     # if request.method == 'POST':  # only true if form is submitted
#     #     form = restapi.forms.CityForm(request.POST)  # add actual request data to form for processing
#     #     form.save()
#     print(Event.objects.all())
#
#
#     return django.http.JsonResponse({'success': True, 'event' event_list})

