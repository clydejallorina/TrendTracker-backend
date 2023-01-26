from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
import json

# Create your views here.

### DUMMY API VIEWS, REMOVE THESE WHEN WE ACTUALLY HAVE PROPER VIEWS
def product_rankings(request):
    rankings = Product.objects.all().order_by("-points")
    ranks = rankings.values("name", "points", "top1post", "top1url", "top1points", "top2post", "top2url", "top2points", "top3post", "top3url", "top3points")
    final_rankings = []
    for rank in ranks:
        data = {}
        data["name"] = rank["name"]
        data["points"] = rank["points"]
        data["posts"] = [
            {"post": rank["top1post"], "url": rank["top1url"], "points": rank["top1points"]},
            {"post": rank["top2post"], "url": rank["top2url"], "points": rank["top2points"]},
            {"post": rank["top3post"], "url": rank["top3url"], "points": rank["top3points"]},
        ]
        final_rankings.append(data)
    print(ranks)
    return HttpResponse(json.dumps(final_rankings))

def user_rankings(request):
    rankings = TiktokUser.objects.all().order_by("-points")
    return HttpResponse(json.dumps(list(rankings.values("username", "points", "positivity", "avatar", "hashtags", "nouns"))))

def hashtags(request):
    pass
