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
    avatar = models.URLField(max_length=256, default="")
    hashtags = models.CharField(max_length=4096, default="")
    nouns = models.CharField(max_length=4096, default="")
    
class TiktokHashtag(models.Model):
    hashtag = models.CharField(max_length=128, default="")
    points = models.BigIntegerField(default=0)

class Product(models.Model):
    name = models.CharField(max_length=256, null=True)
    points = models.BigIntegerField(default=0, null=True)
    description = models.CharField(max_length=2048, null=True)
    url = models.URLField(max_length=256, null=True)
    positivity = models.CharField(max_length=16, default="neutral", null=True)
    top1post = models.CharField(max_length=512, null=True)
    top1url = models.URLField(max_length=256, null=True)
    top1points = models.BigIntegerField(default=0, null=True)
    top2post = models.CharField(max_length=512, null=True)
    top2url = models.URLField(max_length=256, null=True)
    top2points = models.BigIntegerField(default=0, null=True)
    top3post = models.CharField(max_length=512, null=True)
    top3url = models.URLField(max_length=256, null=True)
    top3points = models.BigIntegerField(default=0, null=True)
