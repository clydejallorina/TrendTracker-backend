from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TiktokUser)
admin.site.register(TiktokHashtag)
admin.site.register(Product)