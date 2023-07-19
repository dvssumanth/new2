from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def dvs(request):
    return HttpResponse('game of thrones')
def mohan(request):
    return HttpResponse('clash of clans')