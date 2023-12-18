from django.db import models
from django.utils.translation import gettext_lazy as _


class Flight(models.Model):
    origin = models.CharField(_("مبدا"), max_length=50)
    destination = models.CharField(_("مقصد"), max_length=100)
    slug = models.SlugField(unique=True, allow_unicode=True)
    departed_date = models.DateField(_("تاریخ پرواز"))
    class Passenegrechose(models.TextChoices):
        adult = _('بزرگسال')
        child = _('کودک')
        baby = _('نوزاد')
    passenegre = models.CharField(_("تعداد مسافران"), max_length=7, choices=Passenegrechose.choices, default=Passenegrechose.adult)

    def __str__(self) -> str:
        return str(f'{self.origin} به {self.destination}')

    class Meta:
        db_table = "flight"
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'

class AirLine(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT, related_name='airlines')
    price = models.ForeignKey('Price', on_delete=models.PROTECT, related_name='airlines_price')
    airline_name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, allow_unicode=True)
    airport_type = models.CharField()
    allowed_cargo = models.PositiveSmallIntegerField()
    airport_cabin = models.CharField()
    airport_class = models.CharField()

    class Meta:
        db_table = 'airline'
        verbose_name = 'AirLine'
        verbose_name_plural = 'AirLines'


class Price(models.Model):
    basic_price = models.DecimalField(_("قیمت پایه"), max_digits=15, decimal_places=3)
    taxes_and_duties = models.DecimalField(_("مالیات و عوارض"), max_digits=15, decimal_places=3)
    taxes_and_services = models.DecimalField(_("مالیات و خدمات"), max_digits=15, decimal_places=3)
    value_added_tax = models.DecimalField(_("مالیات بر ارزش افزوده"), max_digits=15, decimal_places=3)
    discount = models.DecimalField(_('تخفیف'), max_digits=15, decimal_places=5)
    
    
    class Meta:
        db_table = 'price'
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'