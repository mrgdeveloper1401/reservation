from decimal import Decimal
from django.dispatch import Signal, receiver
from django.db.models.signals import post_save
from .models import Price


@receiver(post_save,  sender=Price)
def TexesDutise(sender, instance, created, **kwargs):
    if created:
        if instance.passenger_type == 'adult':
            taxes_and_duties = round(Decimal(instance.basic_price / Decimal(9.2)),3)
            instance.save()
            return instance
