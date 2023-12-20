from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.utils.translation import gettext_lazy as _
from core.models import CreateUpdate
from django.core.mail import send_mail
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, CreateUpdate):
    email = models.EmailField(_("ایمیل"), max_length=100, unique=True)
    mobile_phone = models.CharField(_('تلفن همراه '), max_length=11, unique=True)
    first_name =models.CharField(_('نام'), max_length=100)
    last_name = models.CharField(_('نام خوانوادکی'), max_length=100)
    is_staff = models.BooleanField(_('دسترسی کارمندی'), default=False)
    is_active = models.BooleanField(_('کاربر عادی'))
    
    objects = UserManager()

    USERNAME_FIELD = "mobile_phone"
    REQUIRED_FIELDS = ['email']
    
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _('users')