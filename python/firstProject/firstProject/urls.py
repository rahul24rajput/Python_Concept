"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from firstProject import views as fview

urlpatterns = [
    path('newschannel/',include('news.urls')),
    path('admin/', admin.site.urls),
    path('urlApp/' ,include('urlsApp.urls')), # application level url is added to project level 
    path('jobsApp/', include('jobsApp.urls')),# application level url is added to project level 
    path('templateurl/', include('templateProject.urls')),
    
    path('hello/',fview.welcome),
    path('date/',fview.timeInfo),
    
]
