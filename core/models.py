from django.db import models
from django.utils.translation import gettext_lazy as _


class CreateUpdate(models.Model):
    create_at = models.DateTimeField(_('تاریخ ایجاد'), auto_now_add=True, editable=False, blank=True, null=True)
    update_at = models.DateTimeField(_('اخرین بروزرسانی'), auto_now=True, editable=False, blank=True, null=True)
    
    class Meta:
        abstract = True
