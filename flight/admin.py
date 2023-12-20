from django.contrib import admin
from .models import AirLine, FlightAttribute, Flight, Price, FlightAttributeValue


class FlightAttributeValueInline(admin.TabularInline):
    model = FlightAttributeValue
    extra = 0


class PriceInline(admin.StackedInline):
    model = Price
    extra = 0


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    inlines = (FlightAttributeValueInline, PriceInline)
    list_display = ('__str__', 'status_flight', 'flight_start_time', 'flight_end_time', 'origin', 'destination')
    prepopulated_fields = {'slug': ('origin', 'destination')}
    search_fields = ('flight', 'flight_start_time', 'flight_end_time', 'origin', 'destination')
    list_filter = ('status_flight', 'flight_end_time', 'flight_start_time', 'flght_path_choose')
    actions = ('disable_status_flight', 'enable_status_flight')
    
    def disable_status_flight(modeladmin, request, queryset):
        queryset.update(status_flight=False)
        
    def enable_status_flight(modeladmin, request, queryset):
        queryset.update(status_flight=True)
        


@admin.register(AirLine)
class AirLineAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('airline_name',)}
    list_display =('airline_name', 'airport_type', 'allowed_cargo', 'airport_cabin', 'airport_class', 'airport_number_of_seates', 'startus_airline', 'class_cabin_choose', 'airline_rate_choose')
    actions = ('enable_status_airline', 'disable_status_airline')
    search_fields = ('airline_name', )
    list_filter = ('airport_type', 'allowed_cargo', 'airport_cabin', 'startus_airline', 'startus_airline', 'airport_number_of_seates', 'airline_rate_choose', 'class_cabin_choose')

    def enable_status_airline(modeladmin, request, queryset):
        queryset.update(startus_airline=True)
        
    def disable_status_airline(modeladmin, request, queryset):
        queryset.update(startus_airline=False)

@admin.register(FlightAttribute)
class FlightAttributeAdmin(admin.ModelAdmin):
    inlines = (FlightAttributeValueInline,)


@admin.register(FlightAttributeValue)
class FlightAttributeValueAdmin(admin.ModelAdmin):
    pass


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass


    
