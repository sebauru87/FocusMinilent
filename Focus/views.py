from django.http import request
from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'focus/index.html')

def location(request):
    return render(request, 'focus/location.html')

def lab(request):
    return render(request, 'focus/lab.html')
