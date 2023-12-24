from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    roles_choices = [
        ('user', 'USER'),
        ('admin', 'ADMIN'),
    ]
    role = models.CharField(
        max_length=10,
        choices=roles_choices,
        default='user',
        verbose_name='Роль'
    )
    image = models.ImageField(
        upload_to='users/',
        blank=True,
        null=True,
        verbose_name='Аватар'
    )
    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True, null=True, )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.email
