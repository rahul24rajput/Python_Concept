from django.shortcuts import render
from django.http import HttpResponse
import os

def urlAppfirstview(request):
    # current_file_name_and_path = __file__ ## will give the file current file path
    # file_abspath = os.path.abspath(__file__)
    dir_name = os.path.dirname(os.path.abspath(__file__))
    return HttpResponse(dir_name) 