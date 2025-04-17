from django.contrib import admin
from .models import Organization, Event, Participant

admin.site.register(Organization)
admin.site.register(Event)
admin.site.register(Participant)
