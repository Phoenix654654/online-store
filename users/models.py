from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    phone = PhoneNumberField(unique=True)
    password = models.CharField(max_length=50, null=False, blank=False)

    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    is_Vendor = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=6, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.phone)
    

class Vendor(CustomUser):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    ava = models.ImageField(default='default_profile.jpg', upload_to='user/', blank=False)
    is_allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Customer(CustomUser):
    name = models.CharField(max_length=255, null=False, blank=False)
    ava = models.ImageField(default='default_profile.jpg', upload_to='user/', blank=False)

    def __str__(self):
        return self.name
