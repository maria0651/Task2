from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def random2(request):
    return HttpResponse("I am in Third Application.")