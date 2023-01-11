from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class TiktokUser(models.Model):
    username = models.CharField(max_length=128, default="")
    tiktok_id = models.BigIntegerField(default=0)
    points = models.BigIntegerField(default=0)
    positivity = models.CharField(max_length=16, default="neutral")
    url = models.URLField(max_length=256, default="")

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    url = models.URLField(max_length=256)
    positivity = models.CharField(max_length=16, default="neutral")
