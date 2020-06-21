from django.contrib import admin
from .models import ProjectBoard, UnorderedList, Item

admin.site.register(ProjectBoard)
admin.site.register(UnorderedList)
admin.site.register(Item)