from django.urls import path
from jobsApp import views as jviews


urlpatterns = [
path('jobsurl/',jviews.findJob),# Application level url 
]