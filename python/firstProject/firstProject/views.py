from django.shortcuts import render
from django.http import HttpResponse
import datetime


def welcome(request):
    s = '<h1> hello welcome here</h1>'
    return HttpResponse(s)

def timeInfo(request):
    date = datetime.datetime.now()
    msg = '<h1> now server time is </h1>'+str(date)
    return HttpResponse(msg)