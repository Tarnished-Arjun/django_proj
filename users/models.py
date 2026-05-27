from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = (

        ('candidate', 'Candidate'),

        ('employer', 'Employer'),

        ('admin', 'Admin'),
    )

    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    def __str__(self):

        return self.username