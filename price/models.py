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
    discount_price = models.DecimalField(_('تخفیف لحظه ای'), max_digits=15, decimal_places=3, blank=True, null=True,
                                         help_text='بخ صورت لحظه ای ادمین میتواند تخفیف رو اعمل کند', default=0)
    precent_value_added_tax = models.DecimalField(_('مالیات بر ارزش افزوده'), default=0, max_digits=5, decimal_places=2, blank=True, null=True, 
                                                  help_text='به صورت درصدی میتوان وارد کرد')
    # TODO
    precent_taxes_and_services = models.DecimalField(_('مالیات و خدمات'), max_digits=5, decimal_places=2, blank=True, null=True,
                                                     default=0, help_text='به صورت درصدی می توان ان را وارد کرد')
    cansellation_penalty_price = models.DecimalField(_('جریمه کنسلی'), max_digits=5, decimal_places=2, blank=True, null=True,
                                                     help_text='به صورت درصدی میتوان ان را وارد کرد')
    # TODO
    discount = models.ForeignKey(CouponUser, on_delete=models.CASCADE, blank=True, null=True)

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
        
    @property
    def calculate_final_price(self):
        tax_rate = (1 + self.precent_value_added_tax / 100) if self.precent_value_added_tax else 1
        final_price = (self.basic_price - self.discount_price) * tax_rate
        round_final_price = round(final_price, 3)
        return round_final_price
    
    @property
    def calc_cancelled_price(self):
        pay = (self.cansellation_penalty_price / 100) * self.calculate_final_price
        round_pay = round(pay, 3)
        return round_pay

    @property
    def calc_final_price_cancelled(self):
        final_price_calc = self.calculate_final_price - self.calc_cancelled_price
        return final_price_calc

    class Meta:
        db_table = 'price'
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'