from django.contrib import admin
from .models import Image,Notification,Event

# Register your models here.
admin.site.register(Image)
admin.site.register(Notification)
admin.site.register(Event)
