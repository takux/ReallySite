from django.db import models
from django.contrib.auth import get_user_model
import os


def upload_image_to(instance, filename):
    user_id = str(instance.user.id)
    return os.path.join('image', user_id, filename)


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), unique=True, on_delete=models.CASCADE, primary_key=True)

    username = models.CharField(default="匿名ユーザー", max_length=30)

    zipcode = models.CharField(default="", max_length=8)

    prefecture = models.CharField(default="", max_length=6)

    city = models.CharField(default="", max_length=100)

    address = models.CharField(default="", max_length=200)

    image = models.ImageField(default="", blank=True,
                              upload_to=upload_image_to)
