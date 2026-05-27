from django.db import models

from candidate.models import CandidateProfile
from jobs.models import Job


class JobApplication(models.Model):

    STATUS_CHOICES = (

        ('Applied', 'Applied'),

        ('Reviewed', 'Reviewed'),

        ('Rejected', 'Rejected'),

        ('Selected', 'Selected'),
    )

    candidate = models.ForeignKey(
        CandidateProfile,
        on_delete=models.CASCADE
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Applied'
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.candidate} -> {self.job}"