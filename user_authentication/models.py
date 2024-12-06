from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    accept_terms = models.BooleanField(default=False)
    completed = models.BooleanField(default=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField(blank=True)
    alternative_password = models.TextField(blank=True)

    def __str__(self):
        return self.username