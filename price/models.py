from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CreateUpdate
from coupon_management.validations import CouponUser


class Dicount(models.Model):
    # user
    # price
    # uuid
    pass


class Price(CreateUpdate):
    ADULT = 'adult'
    CHILD = 'child'
    BABY = 'baby'
    PASSENGER_TYPES = [
        (ADULT, _('بزرگسال')),
        (CHILD, _('کودک')),
        (BABY, _('نوزاد')),
    ]

    flight = models.ForeignKey('flight.Flight', on_delete=models.PROTECT, related_name='prices')
    passenger_type = models.CharField(_('نوع مسافر'), max_length=10, choices=PASSENGER_TYPES)
    passenegr_number = models.PositiveSmallIntegerField(_('تعداد مسافران'), default=0)
    basic_price = models.DecimalField(_("قیمت پایه"), max_digits=15, decimal_places=3)
    taxes_and_duties = models.DecimalField(_("مالیات و عوارض"), max_digits=15, decimal_places=3, blank=True, null=True)
    taxes_and_services = models.DecimalField(_("مالیات و خدمات"), max_digits=15, decimal_places=3, blank=True, null=True)
    value_added_tax = models.DecimalField(_("مالیات بر ارزش افزوده"), max_digits=15, decimal_places=3, blank=True, null=True)
    discount = models.ForeignKey(CouponUser, on_delete=models.CASCADE)

    @property
    def calculate_texes_and_duties(self):
        if self.passenger_type == 'adult':
            texes = Decimal(self.basic_price /  Decimal(9.2))
            round_texes = round(texes, 3)
            return round_texes
        elif self.passenger_type == 'child':
            texes = (Decimal(self.basic_price /  Decimal(8.8)))
            round_texes = round(texes, 3)
            return round_texes
        else:
            texes = Decimal(self.basic_price / Decimal(6.5))
            round_texes = round(texes, 3)
            return round_texes
        
    def save(self, *args, **kwargs):
        self.texes_and_duties = self.calculate_texes_and_duties
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'price'
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'