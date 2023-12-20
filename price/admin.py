from django.contrib import admin
from .models import Price


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('flight', 'passenger_type', 'passenegr_number', 'basic_price', 'discount_price', 'precent_value_added_tax', 'calculate_final_price', 'cansellation_penalty_price', 'calc_cancelled_price', 'calc_final_price_cancelled')
    list_filter = ('passenger_type', 'create_at', 'update_at',)

