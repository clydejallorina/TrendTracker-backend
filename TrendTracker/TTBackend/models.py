from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class TiktokUser(models.Model):
    username = models.CharField(max_length=128, default="")
    url = models.URLField(max_length=256)

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    url = models.URLField(max_length=256)
