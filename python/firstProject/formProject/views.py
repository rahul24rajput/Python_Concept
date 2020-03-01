from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def studentRegister(request):
    form = forms.StudentRegistration()
    return render(request, 'temProject/register.html',{'form':form})

def FeedBackView(request):
    feedBack = forms.FeedBackForms()
    return render(request,'temProject/feedback.html',{'form':feedBack}) ### Here this form is mandatory if you are not defining context_dict
                                                                        # key should be form mainly    
