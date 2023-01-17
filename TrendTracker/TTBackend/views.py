from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
import json

# Create your views here.

### DUMMY API VIEWS, REMOVE THESE WHEN WE ACTUALLY HAVE PROPER VIEWS
def product_rankings(request):
    test_rankings = [{"1": {"name": "TestProduct", "url": "http://testurl.com/"}}, {"2": {"name": "TestProduct2", "url": "http://testurl.com/"}}]
    return HttpResponse(str(test_rankings))

def user_rankings(request):
    rankings = TiktokUser.objects.all().order_by("-points")
    return HttpResponse(json.dumps(list(rankings.values("username", "points", "positivity", "avatar", "hashtags", "nouns"))))

def hashtags(request):
    pass
