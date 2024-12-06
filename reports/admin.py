from django.contrib import admin
from .models import Location, Mission, Mission_Type
# Register your models here.
admin.site.register(Location)
admin.site.register(Mission_Type)
admin.site.register(Mission)