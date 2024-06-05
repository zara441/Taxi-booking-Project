from django.contrib import admin
from . models import VehicleStand,Location

# Register your models here.
class VehicleStandAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('description',)}
    list_display=["description","address","availability","zoom","price","active"]
    list_editable=["availability","zoom","price","active"]
class LocationAdmin(admin.ModelAdmin):
    list_display=["location","lat","lng"]
    list_editable=["lat","lng"]   

admin.site.register(VehicleStand,VehicleStandAdmin)
admin.site.register(Location,LocationAdmin)
