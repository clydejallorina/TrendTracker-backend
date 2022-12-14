from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.

### DUMMY API VIEWS, REMOVE THESE WHEN WE ACTUALLY HAVE PROPER VIEWS
def product_rankings():
    test_rankings = [{"1": {"name": "TestProduct", "url": "http://testurl.com/"}}, {"2": {"name": "TestProduct2", "url": "http://testurl.com/"}}]
    return HttpResponse(str(test_rankings))

def user_rankings():
    test_rankings = [{"1": {"name": "TestUser", "url": "https://tiktok.com/"}}, {"2": {"name": "TestUser2", "url": "https://tiktok.com/"}}]
    return HttpResponse(str(test_rankings))
