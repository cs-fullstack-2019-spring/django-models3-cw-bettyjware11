# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the exercises index.")

def books(request):
    return HttpResponse('name, pageNumber, genre, publishDate')

def cars(request):
    return HttpResponse('make, model, year')

