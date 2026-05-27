from django.db import models
from users.models import User


class CandidateProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    skills = models.TextField()

    experience = models.IntegerField()

    resume = models.FileField(
        upload_to='resumes/',
        null=True,
        blank=True
    )

    linkedin_url = models.URLField()

    github_url = models.URLField()

    def __str__(self):

        return self.user.username