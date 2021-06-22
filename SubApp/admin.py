from django.contrib import admin

from .models import Subscribers, Invites

# Register your models here.

admin.site.register(Subscribers)
admin.site.register(Invites)