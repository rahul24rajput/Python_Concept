from django.shortcuts import render
from django.http import HttpResponse
from news.models import StudentsTable 

def newsViews(request):
    empData = StudentsTable.objects.all()
    my_dict = {'emp_list':empData} 
    print(empData)
    return render(request,'temProject/news.html',context=my_dict)