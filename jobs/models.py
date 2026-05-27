from django.db import models
from employer.models import EmployerProfile


class Job(models.Model):

    employer = models.ForeignKey(
        EmployerProfile,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    salary = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title