from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from .validators import *


SHORT = 50
BRIEF = 100
MEDIUM = 150
LONG_BRIEF = 200
LONG = 400
VERY_LONG = 1000


class CustomUserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password = None):
        if not email:
            raise ValueError('Users must have a valid e-mail address.')
        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email       = email,
            password    = password,
        )
        user.is_superuser   = True
        user.is_admin       = True
        user.is_staff       = True
        user.save(using = self._db)
        return user


class User(AbstractUser):
    # Remove the default username field.
    username = None
    # Set the User to use email field for authentication.
    USERNAME_FIELD = 'email'
    # User fields.
    email             = models.EmailField   (max_length = SHORT, unique = True)
    first_name        = models.CharField    (max_length = SHORT, validators = [name_validator])
    last_name         = models.CharField    (max_length = SHORT, validators = [name_validator])
    address_street    = models.CharField    (max_length = BRIEF, null = True, blank = True)
    address_suburb    = models.CharField    (max_length = SHORT, null = True, blank = True)
    address_state     = models.CharField    (max_length = SHORT, null = True, blank = True)
    address_postcode  = models.CharField    (max_length = SHORT, null = True, blank = True)
    address_country   = models.CharField    (max_length = SHORT, null = True, blank = True)

    REQUIRED_FIELDS = []

    objects = CustomUserManager()
