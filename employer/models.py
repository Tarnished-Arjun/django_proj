from django.db import models
from users.models import User


class EmployerProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    company_name = models.CharField(
        max_length=255
    )

    company_description = models.TextField()

    location = models.CharField(
        max_length=255
    )

    website = models.URLField()

    def __str__(self):

        return self.company_name