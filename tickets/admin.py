from django.contrib import admin
from .models import PassengerTicket


@admin.register(PassengerTicket)
class PassengerTicketAdmin(admin.ModelAdmin):
    list_display = ('en_first_name', 'en_last_name', 'birth_day', 'gender_choose', 'nation_code')
    list_filter = ('birth_day', 'create_at', 'update_at', 'gender_choose')
    search_fields = ('nation_code',)
