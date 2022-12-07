from django.urls import re_path as url, include

import event.views

app_name = 'event'

urlpatterns = [
    url('^get-all-event/$', event.views.get_all_event, name='get_all_event'),
]