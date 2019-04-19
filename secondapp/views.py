from django.shortcuts import render
from django.http import HttpResponse


def random(request):
    return HttpResponse("I am in Second Application.")
# Create your views here.
