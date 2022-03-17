from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    telephone = models.CharField(max_length=15)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.telephone

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class UserImage(CustomUser):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name="user_images")
    image = models.ImageField(upload_to="static/img/admin_profile_images", null=True, blank=True)
