from django.contrib import admin
from .models import Price,  AirLine, AirLineAttribute

class AirLineAttributeInline(admin.TabularInline):
    model = AirLineAttribute
    extra = 0
    

@admin.register(AirLine)
class FlightDayAdmin(admin.ModelAdmin):
    inlines = (AirLineAttributeInline,)
    prepopulated_fields = {'slug': ('airline_name',)}


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass


@admin.register(AirLineAttribute)
class AirLineAttribute(admin.ModelAdmin):
    pass