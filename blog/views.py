from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def starting_page(request):
    return HttpResponse("response")


def posts(request):
    return HttpResponse("post")


def post_detail(request, post):
    return HttpResponse(post)
