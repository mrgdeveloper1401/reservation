from django.contrib import admin
from .models import Flight, FlightDay


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('origin', 'destination')}


@admin.register(FlightDay)
class FlightDayAdmin(admin.ModelAdmin):
    pass    

    
