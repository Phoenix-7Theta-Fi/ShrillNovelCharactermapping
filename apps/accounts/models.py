from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user',
    )

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=500.00)