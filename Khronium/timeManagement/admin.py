from django.contrib import admin
from .models import DailyList, Event

admin.site.register(DailyList)
admin.site.register(Event)