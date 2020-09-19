from django.urls import path
from urlsApp import views as urlviews


urlpatterns = [
    path('urlappview/',urlviews.urlAppfirstview),
]