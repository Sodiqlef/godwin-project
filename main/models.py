from django.db import models

# Create your models here.


class Hospital(models.Model):
    LOCATION_CHOICES = (
        ('Urban', 'Urban'),
        ('Rural', 'Rural'),
    )

    OWNERSHIP_CHOICES = (
        ('Government', 'Government'),
        ('Private', 'Private'),
        ('Non-Profit', 'Non-Profit'),
    )

    FACILITY_LEVEL_CHOICES = (
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary'),
        ('Tertiary', 'Tertiary'),
    )

    name = models.CharField(max_length=255, verbose_name="Hospital Name")
    location = models.CharField(
        max_length=10, choices=LOCATION_CHOICES, verbose_name="Location")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")
    ownership = models.CharField(
        max_length=15, choices=OWNERSHIP_CHOICES, verbose_name="Ownership")
    ownership_type = models.CharField(
        max_length=255, verbose_name="Ownership Type")
    facility_level = models.CharField(
        max_length=10, choices=FACILITY_LEVEL_CHOICES, verbose_name="Facility Level")
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name="Longitude")
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name="Latitude")
    ambulance_service = models.BooleanField(verbose_name="Ambulance Service")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Hospitals"
