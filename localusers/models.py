from django.contrib.auth.models import AbstractUser
from django.core import serializers
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    telephone = models.CharField(max_length=15)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.telephone

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class UserImage(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/admin_profile_images", null=True, blank=True)