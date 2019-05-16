from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    condo_name = models.CharField(max_length=64, blank=False, default="Not Provided")
    unit = models.CharField(max_length=64, blank=False, default="Not Provided")
    def __str__(self):
        return self.email