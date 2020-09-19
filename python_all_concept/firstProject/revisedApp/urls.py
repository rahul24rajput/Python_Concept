from django.urls import path
from revisedApp import views as reView



urlpatterns = [

    path('hello/',reView.revisedView),
]