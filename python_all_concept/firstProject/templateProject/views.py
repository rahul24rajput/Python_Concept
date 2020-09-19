
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def tempFirstView(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    name= 'rahul rajput'
    mydict = {'date_msg':date,'name':name,'hour':h,}
    return render(request,'temProject/temp.html', context=mydict)

def profileView(request):
    user= 'rahul rajput'
    myProfile = {'user':user}
    return render(request, 'temProject/profile.html',context=myProfile)