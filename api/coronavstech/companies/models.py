"""File used to generate Django Models
"""
from django.db import models
from django.utils.timezone import now


class Company(models.Model):
    """Company Model
    """

    class CompanyStatus(models.TextChoices):
        """Pre-defined Choices for status in Company
        """
        LAYOFFS = 'Layoffs'
        HIRING_FREEZE = 'Hiring Freeze'
        HIRING = 'Hiring'

    name = models.CharField(max_length=30, unique=True)
    status = models.CharField(choices=CompanyStatus.choices,
                              default=CompanyStatus.HIRING,
                              max_length=30)
    last_update = models.DateTimeField(default=now, editable=True)
    application_link = models.URLField(blank=True)
    notes = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f'{self.name}'
