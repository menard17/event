from django.db import models

class Event(models.Model):
    objects = None
    event_name = models.CharField(max_length=200)
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()

    def serialized(self):
        return {
            'id': self.pk,
            'name': self.event_name,
            'start': self.event_start,
            'end': self.event_end
        }
