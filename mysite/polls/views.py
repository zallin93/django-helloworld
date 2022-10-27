from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request): 
    return HttpResponse("Hello, world. You're at the poll index!")

def president_2024(request):
    return HttpResponse("Who will win the 2024 election? ")