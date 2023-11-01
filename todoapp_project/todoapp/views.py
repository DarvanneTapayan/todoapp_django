from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello, World!")


def index(request):
    return HttpResponse("this is the index page")
