from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
import random
import string

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _generate_random_username(self):
        """Generate a random 9-digit number."""
        random_number = ''.join(random.choices(string.digits, k=9))
        return '309' + random_number  # Adding '309' as prefix

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('username', self._generate_random_username())
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=9, default=CustomUserManager()._generate_random_username, unique=True)

    USERNAME_FIELD = 'email'  # Foydalanuvchilar email orqali login qila oladilar
    REQUIRED_FIELDS = ['username']  # username kerakli maydon

    objects = CustomUserManager()