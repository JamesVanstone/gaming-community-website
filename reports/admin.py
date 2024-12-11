from django.contrib import admin
from .models import Location, Mission, Mission_Type
# Register your models here.
admin.site.register(Location)
admin.site.register(Mission_Type)

class MissionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "location", "date", "type", "pay", "approved", "author")
    list_editable = ("location", "date", "type", "pay", "approved", "author")

admin.site.register(Mission, MissionAdmin)