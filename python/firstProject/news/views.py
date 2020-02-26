from django.shortcuts import render
from django.http import HttpResponse


def newsViews(request):
    return HttpResponse('<h1>My name is rahul</h1>')