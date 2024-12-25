from django.contrib import admin
from .models import Client, Status, Place
# Register your models here.

admin.site.register(Client)
admin.site.register(Status)
admin.site.register(Place)