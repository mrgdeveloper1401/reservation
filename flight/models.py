from django.db import models
from django.utils.translation import gettext_lazy as _


class AirLine(models.Model):
    airline_name = models.CharField(_('نام شرکت هواپیما'), max_length=64)
    slug = models.SlugField(unique=True, allow_unicode=True)
    airport_type = models.CharField(_('نوع هواپیما'), max_length=50)
    allowed_cargo = models.PositiveSmallIntegerField(_('بار مجاز'))
    airport_cabin = models.CharField(_('کابین'), max_length=50)
    airport_class = models.CharField(_('کلاس نرخی'), max_length=50)
    price = models.ForeignKey('Price', on_delete=models.PROTECT, related_name='airlines_price')

    class Meta:
        db_table = 'airline'
        verbose_name = 'AirLine'
        verbose_name_plural = 'AirLines'


class AirLineAttribute(models.Model):
    airline = models.ForeignKey(AirLine, on_delete=models.PROTECT, related_name='airline_attribute')
    attribute = models.CharField(_('ويژگی'), max_length=50)
    value_char = models.CharField(_('مقدار'), max_length=50)
    value_text = models.CharField(_("مقدار متنی"), max_length=50)
    value_datetime = models.DateTimeField(_('مقدار زمانی'))
    
    
    class Meta:
        db_table = 'airline attribute'
        verbose_name = 'airline attribute'
        verbose_name_plural = 'airline attributes'


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



class Ticket(models.Model):
    pass