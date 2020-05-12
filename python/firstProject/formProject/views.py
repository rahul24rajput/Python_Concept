from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def studentRegister(request):
    form = forms.StudentRegistration()
    return render(request, 'temProject/register.html',{'form':form})
def RenderedDaaView(request):
    # print(request.data)
    return render(request,'temProject/render_Data.html')

def FeedBackView(request):
    if request.method=="GET":
        feedBack = forms.FeedBackForms()
        return render(request,'temProject/feedback.html',{'form':feedBack})
    if request.method == 'POST':
        form = forms.FeedBackForms(request.POST)
        if form.is_valid():
            print('From validation success')
            # if t
            # How to capture the data enter by end user
            # So for that we have to use cleaned_data ## type is dictaniory 
            # {'name': Data entered,} Key will be the same you have defined in forms.py and value will be
            # the data has been entered by user you called is_valid method
            # Note : cleaned data can be used after 
            print('Student Name', form.cleaned_data['name'])
            print('Student Name', form.cleaned_data['rollno'])
            print('Student Name', form.cleaned_data['email'])
            print('Student Name', form.cleaned_data['feedback'])
            # render_dict = {'name':form.cleaned_data['name']}
            ## rendering the data in new html file bcz print will print it on console
            return RenderedDaaView(request) # this is how you call another view from one view
            
    ### Here this form is mandatory if you are not defining context_dict
                                                                        # key should be form mainly    
