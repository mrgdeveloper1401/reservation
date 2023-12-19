from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CreateUpdate


class AirLine(CreateUpdate):
    airline_name = models.CharField(_('نام شرکت هواپیما'), max_length=64)
    airline_image = models.ImageField(_('عکس'), blank=True, null=True, upload_to='airline/%Y/%M/%d')
    slug = models.SlugField(unique=True, allow_unicode=True)
    airport_type = models.CharField(_('نوع هواپیما'), max_length=50)
    allowed_cargo = models.PositiveSmallIntegerField(_('بار مجاز'))
    airport_cabin = models.CharField(_('نوع کابین'), max_length=50)
    airport_class = models.CharField(_('کلاس نرخی'), max_length=50)
    airport_number_of_seates = models.PositiveIntegerField(_('تعداد صندلی های هواپمیا'))
    startus_airline = models.BooleanField(_("وضعیت شرکت هواپیمایی"), default=True)
    class ClassCabin(models.TextChoices):
        # Economy or economy class is known as the normal class of travel.
        Economy =  'Economy', _('کلاس اقتصادی')
        # Business class has larger travel space, more comfortable seats, and more advanced services.
        Business = 'Business', _('کلاس کسب و کار')
        # First class is the highest level of travel on some planes.
        # This class often features private travel space, luxury bedding, high quality menus, and personalized service.
        First = 'First',  _('کلاس اول')
    class_cabin_choose = models.CharField(_('کلاس هواپیما'), max_length=8, choices=ClassCabin.choices, default=ClassCabin.Economy)
    
    class AirlineRate(models.TextChoices):
        special = 'scpecial', _('نرخ ويژه')
        normal = 'normal', _('نرخ عادی')
    airline_rate_choose = models.CharField(_('نوع نرخ هواپیما'), max_length=8, choices=AirlineRate.choices, default=AirlineRate.normal)
    
    def __str__(self) -> str:
        return self.airline_name
    
    class Meta:
        db_table = 'airline'
        verbose_name = 'AirLine'
        verbose_name_plural = 'AirLines'


class Flight(CreateUpdate):
    aairline = models.ForeignKey(AirLine, on_delete=models.PROTECT,related_name = 'flights', verbose_name='پرواز')
    origin = models.CharField(_('مبدا'), max_length=50)
    destination = models.CharField(_('مقصد'), max_length=50)
    slug = models.SlugField(unique=True, allow_unicode=True)
    flight_start_time = models.DateTimeField(_('ساعت پرواز'))
    flight_end_time = models.DateTimeField(_('ساعت فرود'))
    status_flight = models.BooleanField(_("وضعیت پرواز"))

    def __str__(self) -> str:
        return f'شرکت هواپیمایی {self.aairline.airline_name}پرواز از مبدا {self.origin} به مقصد {self.destination}'
    
    class Meta:
        db_table = "flight"
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'


class FlightAttribute(CreateUpdate):
    attribute = models.CharField(_('ويژگی'), max_length=50)

    def __str__(self) -> str:
        return self.attribute

    class Meta:
        db_table = 'airline attribute'
        verbose_name = 'airline attribute'
        verbose_name_plural = 'airline attributes'


class FlightAttributeValue(CreateUpdate):
    attribute = models.ForeignKey(FlightAttribute, on_delete=models.PROTECT, related_name='attributes')
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT, related_name='flight_attribute_values')
    atribute_value = models.CharField(_('مقدار ويژگی'),  max_length=100)
    
    def __str__(self) -> str:
        return f'{self.attribute.attribute} -- {self.atribute_value}'

    class Meta:
        db_table = "flight_attribute_value"        
        verbose_name = 'FlightAttributeValue'
        verbose_name_plural = 'FlightAttributeValues'
    
    
class Price(CreateUpdate):
    ADULT = 'adult'
    CHILD = 'child'
    BABY = 'baby'
    PASSENGER_TYPES = [
        (ADULT, _('بزرگسال')),
        (CHILD, _('کودک')),
        (BABY, _('نوزاد')),
    ]

    flight = models.ForeignKey(Flight, on_delete=models.PROTECT, related_name='prices')
    passenger_type = models.CharField(_('نوع مسافر'), max_length=10, choices=PASSENGER_TYPES)
    passenegr_number = models.PositiveSmallIntegerField(_('تعداد مسافران'), default=0)
    basic_price = models.DecimalField(_("قیمت پایه"), max_digits=15, decimal_places=3)
    taxes_and_duties = models.DecimalField(_("مالیات و عوارض"), max_digits=15, decimal_places=3, blank=True, null=True)
    taxes_and_services = models.DecimalField(_("مالیات و خدمات"), max_digits=15, decimal_places=3, blank=True, null=True)
    value_added_tax = models.DecimalField(_("مالیات بر ارزش افزوده"), max_digits=15, decimal_places=3, blank=True, null=True)
    discount = models.DecimalField(_('تخفیف'), max_digits=15, decimal_places=5,  blank=True, null=True)

    class Meta:
        db_table = 'price'
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'
