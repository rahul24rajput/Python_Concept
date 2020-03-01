from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def studentRegister(request):
    form = forms.StudentRegistration()
    return render(request, 'temProject/register.html',{'form':form})

def FeedBackView(request):
    feedBack = forms.FeedBackForms()
    if request.method == 'POST':
        form = forms.FeedBackForms(request.POST)
        if form.is_valid():
            print('From validation success')
            # How to capture the data enter by end user
            # So for that we have to use cleaned_data ## type is dictaniory 
            # {'name': Data entered,} Key will be the same you have defined in forms.py and value will be
            # the data has been entered by user
            print('Student Name', form.cleaned_data['name'])
            print('Student Name', form.cleaned_data['rollno'])
            print('Student Name', form.cleaned_data['email'])
            print('Student Name', form.cleaned_data['feedback'])
    return render(request,'temProject/feedback.html',{'form':feedBack}) ### Here this form is mandatory if you are not defining context_dict
                                                                        # key should be form mainly    
