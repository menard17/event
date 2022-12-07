import datetime

import django.forms
from dateutil.parser import *
from django.core.exceptions import ValidationError

import event.models


class EventForm(django.forms.ModelForm):
    event_name = django.forms.Field(required=True)
    event_start = django.forms.Field(required=True)
    event_end = django.forms.Field(required=True)

    class Meta:
        model = event.models.Event

    def overlapping_time(self, start, end):
        offset =datetime.timedelta(minutes=14, seconds=59)
        start = dateutil.parser.parse(start) - offset
        end = dateutil.parser.parse(start) - offset


    def clean_event_start(self):
        event_start = self.data.get('event_start', None)
        if not event_start:
            raise ValidationError('Please fill out start field.')
        date_start =dateutil.parser.parse(event_start)
        if self._is_past_date(date_start):
            raise ValidationError('Could not schedule a past date')

    def clean_event_end(self):
        event_start = self.data.get('event_end', None)
        if not event_start:
            raise ValidationError('Please fill out start field.')
        date_start =dateutil.parser.parse(event_start)
        if self._is_past_date(date_start):
            raise ValidationError('Could not schedule a past date')

    def validation(self, start, end):
        offset =datetime.timedelta(minutes=14, seconds=59)
        start = dateutil.parser.parse(start) - offset
        end = dateutil.parser.parse(end) - offset
        if start >= 8 and end <= 20:
          return True
        if self._is_past_date(start):
            raise ValidationError('Could not schedule a past date')


    def _is_past_date(self, date):
        if not date:
            return False
        now = datetime.datetime.now()
        if django.utils.timezone.is_naive(now):
            now = django.utils.timezone.make_aware(now)
        if django.utils.timezone.is_naive(date):
            date = django.utils.timezone.make_aware(date)
        return date < now

