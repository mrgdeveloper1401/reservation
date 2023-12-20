from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CreateUpdate
from django_countries.fields import CountryField

class PassengerTicket(CreateUpdate):
    en_first_name = models.CharField(_('نام فارسی لاتین' ), max_length=100)
    en_last_name = models.CharField(_('نام خانوادگی به لاتین'), max_length=100)
    birth_day = models.DateField(_('تاریخ تولد'))
    
    class Gender(models.TextChoices):
        male = 'male', _('مرد'),
        female = 'female', _('زن')
    gender_choose = models.CharField(_('نوع جنسیت'), max_length=6, choices=Gender.choices)
    nation_code = models.CharField(_('کد ملی'), max_length=11, unique=True)
    # TODO 
    # fix bug no attribute __len__
    # nationality = CountryField()