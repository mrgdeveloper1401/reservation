from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from django.contrib.auth.hashers import make_password

class UserManager(UserManager):
    
    def create_user(self, mobile_phone, email, password=None):
        if not mobile_phone:
            raise ValueError('Mobile phone must be set')
        if not email:
            raise ValueError('Email must be set')
        user = self.model(
            mobile_phone=mobile_phone,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, mobile_phone, email, password=None):
        user = self.create_user(
            email=email,
            mobile_phone=mobile_phone,
            password=password
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True  # تغییر اینجا
        user.save(using=self._db)
        return user
