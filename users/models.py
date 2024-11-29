from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {
    'blank': True,
    'null': True,
}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=150, default='anonym', verbose_name='first_name')
    last_name = models.CharField(max_length=150, default='anonym', verbose_name='last_name')
    phone = models.CharField(unique=True, max_length=20, verbose_name='phone', **NULLABLE)
    telegram = models.CharField(unique=True, max_length=100, verbose_name='telegram', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='active')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']
