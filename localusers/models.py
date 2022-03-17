from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    # image = models.ImageField(upload_to="static/img/admin_profile_images", null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
