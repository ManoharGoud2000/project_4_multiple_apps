from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def firstapp_first(request):
    return HttpResponse('<h1><marquee>1st App 1st function</marquee></h1>')

def second_second(request):
    return HttpResponse('<h1><marquee>1st App 2nd function</marquee></h1>')