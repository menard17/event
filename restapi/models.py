from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
